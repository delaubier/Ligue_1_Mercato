# Ligue 1 Mercato ⚽🤖

<p align="left">
  <a href="https://x.com/Ligue_1_Mercato" target="_blank">
    <img src="https://img.shields.io/badge/X-@Ligue__1__Mercato-000000?style=for-the-badge&logo=x&logoColor=white" alt="Compte X" />
  </a>
  <img src="https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.9+" />
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="License" />
</p>

🌐 **Langue / Language** : **Français 🇫🇷** • [English 🇬🇧](README.en.md)

---

Bot Twitter (X) automatique développé en Python qui détecte et publie en temps réel les officialisations de transferts de football en Ligue 1 en scrapant les données sur [Transfermarkt](https://www.transfermarkt.fr).

Suivez le bot en direct sur X / Twitter : **[@Ligue_1_Mercato](https://x.com/Ligue_1_Mercato)**

---

## 📌 Fonctionnalités

- **Scraping automatique** : Récupère les derniers transferts de Ligue 1 (joueur, clubs, montant ou type de transfert, âge, nationalité, etc.).
- **Publication Twitter enrichie** : Formate et poste des annonces avec émojis (drapeau, officiel, contrat) et la photo officielle du joueur.
- **Détection des doublons** : Évite de tweeter deux fois le même transfert.
- **Sécurité** : Clés d'API gérées en toute sécurité via variables d'environnement (`.env`).

---

## 🚀 Installation

### 1. Cloner le projet
```bash
git clone https://github.com/delaubier/Ligue_1_Mercato.git
cd Ligue_1_Mercato
```

### 2. Installer les dépendances
```bash
pip install -r requirements.txt
```

### 3. Configurer les clés Twitter
Créez un fichier `.env` à la racine en copiant le modèle `.env.example` :
```bash
cp .env.example .env
```

Remplissez ensuite vos clés d'API Twitter dans le fichier `.env` :
```env
TWITTER_CONSUMER_KEY=votre_cle_api
TWITTER_CONSUMER_SECRET=votre_secret_api
TWITTER_ACCESS_TOKEN=votre_access_token
TWITTER_ACCESS_TOKEN_SECRET=votre_access_token_secret
```

---

## 🏃 Utilisation

Pour lancer le bot en local :
```bash
python bot.py
```

---

## ☁️ Déploiement

Le projet inclut un fichier [`Procfile`](Procfile) permettant un déploiement continu en tant que *worker* sur des plateformes cloud comme Heroku, Railway ou Render.