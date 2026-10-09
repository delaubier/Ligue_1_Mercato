# Ligue 1 Mercato

### Moteur de Suivi Automatisé des Transferts et de Notification en Temps Réel pour la Ligue 1 sur X/Twitter

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![X](https://img.shields.io/badge/X-@Ligue__1__Mercato-000000.svg)](https://x.com/Ligue_1_Mercato)

🌐 **Langue / Language** : **Français 🇫🇷** • [English 🇬🇧](README.md)

---

Un bot Python automatisé qui surveille, analyse et diffuse en temps réel les officialisations de transferts de football en Ligue 1 à partir des données extraites de [Transfermarkt](https://www.transfermarkt.fr).

Suivez le bot en direct sur X / Twitter : **[@Ligue_1_Mercato](https://x.com/Ligue_1_Mercato)**

---

## Fonctionnalités

Dans la couverture médiatique et l'analyse du football moderne, le suivi manuel des annonces officielles de transfert à travers plusieurs clubs et sources nécessite un temps considérable et engendre des retards de publication.

**Ligue 1 Mercato** automatise ce flux de travail :
- **Réduit le temps de veille de 100%** en scrapant Transfermarkt en continu pour une détection instantanée des officialisations.

- **Formate des publications enrichies** incluant la photo officielle du joueur, des métadonnées structurées (nationalité, âge, montant, durée de contrat) et des visuels adaptés.

- **Évite la diffusion de doublons** grâce à un registre d'historique de transactions local.

- **Sécurise les identifiants d'API** via un cloisonnement strict des variables d'environnement (`.env`).

---

## Installation

### 1. Cloner le dépôt
```bash
git clone https://github.com/delaubier/Ligue_1_Mercato.git
cd Ligue_1_Mercato
```

### 2. Installer les dépendances
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

pip install -r requirements.txt
```

### 3. Configurer les clés d'API Twitter
Créez un fichier `.env` à la racine en copiant le modèle `.env.example` :
```bash
cp .env.example .env
```

Renseignez vos clés d'API Twitter dans le fichier `.env` :
```env
TWITTER_CONSUMER_KEY=votre_cle_api
TWITTER_CONSUMER_SECRET=votre_secret_api
TWITTER_ACCESS_TOKEN=votre_access_token
TWITTER_ACCESS_TOKEN_SECRET=votre_access_token_secret
```

---

## Utilisation

### Lancer le Bot en Local
Exécute le service de surveillance continue et de publication :

```bash
python bot.py
```

---

## Déploiement Cloud

Le dépôt inclut un fichier [`Procfile`](Procfile) prêt à l'emploi pour un déploiement continu en tâche de fond (*worker*) 24/7 sur des plateformes cloud comme Heroku, Railway ou Render.

---

## Licence

Distribué sous la licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus de détails.
