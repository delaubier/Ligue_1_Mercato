# Ligue 1 Mercato

### Automated Transfer Tracking and Real-Time X/Twitter Notification Engine for Ligue 1

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![X](https://img.shields.io/badge/X-@Ligue__1__Mercato-000000.svg)](https://x.com/Ligue_1_Mercato)

🌐 **Language / Langue** : **English 🇬🇧** • [Français 🇫🇷](README.md)

---

An automated Python bot that monitors, parses, and broadcasts official French Ligue 1 football transfer market updates in real time using data extracted from [Transfermarkt](https://www.transfermarkt.fr).

Follow the bot live on X / Twitter: **[@Ligue_1_Mercato](https://x.com/Ligue_1_Mercato)**

---

## Features

In modern football analytics and media coverage, manually tracking official transfer announcements across multiple clubs and sources is time-consuming and prone to delays.

**Ligue 1 Mercato** automates this workflow:
- **Reduces tracking overhead by 100%** by scraping Transfermarkt continuously for instant deal detection.

- **Formats rich social publications** with official player media, structured metadata (nationality, age, fee, contract duration), and tailored visuals.

- **Prevents duplicate broadcasting** using a localized transaction history registry.

- **Secures API credentials** via robust environment variable isolation (`.env`).

---

## Installation

### 1. Clone the repository
```bash
git clone https://github.com/delaubier/Ligue_1_Mercato.git
cd Ligue_1_Mercato
```

### 2. Install dependencies
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

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

## Usage

### Run the Bot Locally
Executes the continuous monitoring and posting service:

```bash
python bot.py
```

---

## Cloud Deployment

The repository includes a [`Procfile`](Procfile) ready for 24/7 background worker deployment on cloud platforms such as Heroku, Railway, or Render.

---

## License

Distributed under the MIT License. See [LICENSE](LICENSE) for details.
