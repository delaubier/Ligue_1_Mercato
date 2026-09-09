"""
bot.py - Ligue 1 Mercato Twitter Bot
------------------------------------
Ce script surveille en continu la page des derniers transferts de Ligue 1
sur Transfermarkt et publie automatiquement une annonce sur Twitter (X)
pour chaque nouveau transfert détecté.
"""

import os
import time
import logging
import io
import re
import urllib.request
from typing import Optional, Dict

import requests
import tweepy
from bs4 import BeautifulSoup
from PIL import Image

# ==========================================
# CONSTANTES ET CONFIGURATION
# ==========================================
# Configuration du système de journalisation (logs)
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - [%(levelname)s] - %(message)s'
)

URL_TRANSFERS = "https://www.transfermarkt.fr/ligue-1/letztetransfers/wettbewerb/FR1/plus/1"
URL_GALLERY = "https://www.transfermarkt.fr/ligue-1/letztetransfers/wettbewerb/FR1/galerie/1"
BASE_URL = "https://www.transfermarkt.fr"

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

# Dictionnaire des drapeaux
FLAGS = {
    "France": "🇫🇷",
    "Turquie": "🇹🇷",
    "Brésil": "🇧🇷",
    "Espagne": "🇪🇸",
    "Portugal": "🇵🇹",
    "Italie": "🇮🇹",
    "Allemagne": "🇩🇪",
    "Angleterre": "🇬🇧",
    "Belgique": "🇧🇪",
    "Pays-Bas": "🇳🇱",
    "Argentine": "🇦🇷"
}
DEFAULT_FLAG = ""

# URL de l'image par défaut (placeholder) de Transfermarkt à ignorer
PLACEHOLDER_IMAGE_URL = "https://tmssl.akamaized.net/images/galerie_bg.jpg"

# Fréquence de rafraîchissement
CHECK_INTERVAL_SECONDS = 300  # 5 minutes


# ==========================================
# FONCTIONS UTILITAIRES
# ==========================================
def load_environment() -> None:
    """Charge les variables d'environnement depuis le fichier .env"""
    try:
        from dotenv import load_dotenv
        load_dotenv()
    except ImportError:
        if os.path.exists(".env"):
            with open(".env", "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith("#") and "=" in line:
                        key, value = line.split("=", 1)
                        os.environ.setdefault(key.strip(), value.strip())

def authenticate_twitter() -> tweepy.API:
    """Initialise et retourne le client API Twitter"""
    consumer_key = os.getenv("TWITTER_CONSUMER_KEY")
    consumer_secret = os.getenv("TWITTER_CONSUMER_SECRET")
    access_token = os.getenv("TWITTER_ACCESS_TOKEN")
    access_token_secret = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")

    if not all([consumer_key, consumer_secret, access_token, access_token_secret]):
        raise ValueError("Clés d'API manquantes dans le fichier .env.")

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    return tweepy.API(auth)


def get_latest_transfer() -> Optional[Dict[str, str]]:
    """
    Extrait le transfert le plus récent de la page web Transfermarkt
    """
    try:
        # Récupération de la page web avec un timeout de sécurité
        res = requests.get(URL_TRANSFERS, headers=HEADERS, timeout=10)
        res_gal = requests.get(URL_GALLERY, headers=HEADERS, timeout=10)
        res.raise_for_status()
        res_gal.raise_for_status()

        soup = BeautifulSoup(res.content, 'html.parser')
        soup_gal = BeautifulSoup(res_gal.content, 'html.parser')

        # Trouver le premier transfert dans le tableau principal
        table = soup.find('table', {'class': 'items'})
        if not table:
            logging.error("Tableau des transferts introuvable.")
            return None
            
        tbody = table.find('tbody')
        if not tbody:
            return None
            
        rows = tbody.find_all('tr', recursive=False)
        if not rows:
            return None
            
        first_row = rows[0]
        cols = first_row.find_all('td', recursive=False)
        if len(cols) < 7:
            logging.error("Structure du tableau inattendue.")
            return None

        # Joueur
        player_links = cols[0].find_all('a')
        player_name = player_links[1].text.strip() if len(player_links) > 1 else 'Inconnu'
        profile_url = BASE_URL + player_links[1]['href'] if len(player_links) > 1 else BASE_URL
        
        # ID
        m = re.search(r'/spieler/(\d+)', profile_url)
        player_id = m.group(1) if m else player_name

        # Poste
        pos_td = cols[0].find_all('tr')
        poste = pos_td[-1].text.strip() if pos_td else 'Inconnu'

        # Nationalité
        nat_img = cols[1].find('img', {'class': 'flaggenrahmen'})
        nationality = nat_img['title'] if nat_img else 'Inconnu'

        # Age
        age = cols[2].text.strip()

        # Club de départ
        club_from_links = cols[3].find_all('a')
        club_from = club_from_links[1].text.strip() if len(club_from_links) > 1 else 'Inconnu'

        # Club d'arrivée
        club_to_links = cols[4].find_all('a')
        club_to = club_to_links[1].text.strip() if len(club_to_links) > 1 else 'Inconnu'
        ligue_to = club_to_links[-1].text.strip() if len(club_to_links) > 2 else 'Inconnue'

        # Valeur du transfert
        transfer_value = cols[6].text.strip()

        # URL de l'image
        image_url = ""
        nodes_images = soup_gal.find_all("div", {"class": "galerie-bild-container"})
        if nodes_images:
            img_tag = nodes_images[0].find("img", {"class": "galerie-bild"})
            if img_tag and 'src' in img_tag.attrs:
                src = img_tag['src'].strip()
                if src and "galerie_bg.jpg" not in src and src != PLACEHOLDER_IMAGE_URL:
                    image_url = src
                else:
                    logging.info("Image générique détectée (galerie_bg.jpg) : ignorée.")

        # Visite de la page profil pour récupérer la durée du contrat
        contract_end = "??"
        if profile_url != BASE_URL:
            res_profil = requests.get(profile_url, headers=HEADERS, timeout=10)
            if res_profil.status_code == 200:
                soup_profil = BeautifulSoup(res_profil.content, 'html.parser')
                nodes_contrat = soup_profil.find_all("td", {"class": "zentriert"})
                if len(nodes_contrat) > 1:
                    contract_end = nodes_contrat[1].text.strip()

        return {
            "id": player_id,
            "name": player_name,
            "value": transfer_value,
            "club_from": club_from,
            "club_to": club_to,
            "age": age,
            "poste": poste,
            "ligue_to": ligue_to,
            "nationality": nationality,
            "contract_end": contract_end,
            "profile_url": profile_url,
            "image_url": image_url
        }

    except Exception as e:
        logging.error(f"Erreur lors du scraping des données : {e}")
        return None


def download_media(url: str) -> Optional[io.BufferedReader]:
    """
    Télécharge une image distante et la prépare en mémoire (format PNG).
    Évite de créer des fichiers résiduels sur le disque.
    Ignore l'URL placeholder de Transfermarkt.
    """
    if not url or "galerie_bg.jpg" in url or url == PLACEHOLDER_IMAGE_URL:
        return None
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=10) as response:
            image_data = response.read()
            
        img = Image.open(io.BytesIO(image_data))
        buffer = io.BytesIO()
        img.save(buffer, format="PNG")
        buffer.seek(0)
        return io.BufferedReader(buffer)
    except Exception as e:
        logging.error(f"Impossible de télécharger l'image depuis {url} : {e}")
        return None


def format_tweet(transfer: Dict[str, str]) -> str:
    """Génère le texte final du tweet à partir des données structurées."""
    flag = FLAGS.get(transfer["nationality"], DEFAULT_FLAG)
    name = transfer["name"]
    poste = transfer["poste"]
    age = transfer["age"]
    club_from = transfer["club_from"]
    club_to = transfer["club_to"]
    ligue_to = transfer["ligue_to"]
    val = transfer["value"]
    contract = transfer["contract_end"]
    link = transfer["profile_url"]

    # Message du tweet
    flag_prefix = f"{flag} " if flag else ""
    header = f"🔴 OFFICIEL 🔴\n\n{flag_prefix}{name} ({poste} de {age} ans)"
    
    if val == "Prêt":
        body = f"est prêté à {club_to} ({ligue_to}) jusqu'au {contract} en provenance de {club_from} !"
    elif val in ["?", "Transfert libre", "-", "Fin du prêt"]:
        body = f"est transféré à {club_to} ({ligue_to}) en provenance de {club_from} pour un montant non dévoilé / libre !"
    else:
        body = f"est transféré à {club_to} ({ligue_to}) en provenance de {club_from} pour {val} !"
        
    footer = f"\n\n➡ {link}"
    
    return f"{header} {body}{footer}"


# ==========================================
# ENTRY POINT
# ==========================================
def main():
    load_environment()
    
    try:
        api = authenticate_twitter()
        api.verify_credentials()
        logging.info("Connexion à l'API Twitter réussie.")
    except Exception as e:
        logging.critical(f"Erreur d'authentification Twitter : {e}")
        return

    # Pour ne pas tweeter deux fois le même transfert
    last_processed_id = None

    logging.info("Bot démarré. En attente de transferts...")

    while True:
        logging.info("Vérification en cours...")
        transfer = get_latest_transfer()
        
        if transfer is not None:
            current_id = transfer["id"]
            
            # Au premier lancement, on initialise l'état avec le dernier transfert connu
            # pour éviter de publier de vieux transferts passés.
            if last_processed_id is None:
                last_processed_id = current_id
                logging.info(f"État initialisé avec le dernier transfert connu : {transfer['name']} ({current_id})")
                
            # Un nouveau transfert inédit
            elif current_id != last_processed_id:
                logging.info(f"✨ Nouveau transfert trouvé : {transfer['name']} vers {transfer['club_to']}")
                
                tweet_text = format_tweet(transfer)
                logging.info(f"Contenu du tweet :\n{tweet_text}")
                
                try:
                    media_ids = None
                    if transfer["image_url"]:
                        img_file = download_media(transfer["image_url"])
                        if img_file:
                            media = api.media_upload('transfer.png', file=img_file)
                            media_ids = [media.media_id]
                    
                    # Publication officielle
                    api.update_status(status=tweet_text, media_ids=media_ids)
                    logging.info("✅ Tweet publié avec succès !")
                    
                    # Mise à jour de l'état (uniquement si le tweet a réussi)
                    last_processed_id = current_id
                    
                except Exception as e:
                    logging.error(f"Échec de l'envoi du tweet : {e}")
                    last_processed_id = current_id
            else:
                logging.info("Aucun nouveau transfert pour le moment.")
        
        logging.info(f"En attente de {CHECK_INTERVAL_SECONDS} secondes avant le prochain check...")
        time.sleep(CHECK_INTERVAL_SECONDS)


if __name__ == "__main__":
    main()