# Ligue 1 Mercato ⚽🤖

<p align="left">
  <a href="https://x.com/Ligue_1_Mercato" target="_blank">
    <img src="https://img.shields.io/badge/X-@Ligue__1__Mercato-000000?style=for-the-badge&logo=x&logoColor=white" alt="X Account" />
  </a>
  <img src="https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.9+" />
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="License" />
</p>

🌐 **Language / Langue** : [Français 🇫🇷](README.md) • **English 🇬🇧**

---

Automated Twitter (X) bot written in Python that detects and publishes French Ligue 1 official football transfers in real-time by scraping data from [Transfermarkt](https://www.transfermarkt.fr).

Follow the bot live on X / Twitter: **[@Ligue_1_Mercato](https://x.com/Ligue_1_Mercato)**

---

## 📌 Features

- **Automated Web Scraping**: Fetches the latest Ligue 1 transfers (player, departing/arriving clubs, transfer fee or loan terms, age, nationality, etc.).
- **Rich Twitter Posts**: Automatically formats and publishes announcements with emojis (country flags, contract details) and player pictures.
- **Duplicate Prevention**: Keeps track of recent posts to ensure no transfer is tweeted twice.
- **Security**: Secret API credentials safely managed using environment variables (`.env`).

---

## 🚀 Installation

### 1. Clone the repository
```bash
git clone https://github.com/delaubier/Ligue_1_Mercato.git
cd Ligue_1_Mercato
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure Twitter API Credentials
Create a `.env` file at the root by copying `.env.example`:
```bash
cp .env.example .env
```

Fill in your Twitter API keys inside `.env`:
```env
TWITTER_CONSUMER_KEY=your_consumer_key
TWITTER_CONSUMER_SECRET=your_consumer_secret
TWITTER_ACCESS_TOKEN=your_access_token
TWITTER_ACCESS_TOKEN_SECRET=your_access_token_secret
```

---

## 🏃 Usage

Run the bot locally:
```bash
python bot.py
```

---

## ☁️ Cloud Deployment

The repository includes a [`Procfile`](Procfile) ready for 24/7 background worker deployment on cloud platforms such as Heroku, Railway, or Render.
