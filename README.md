# Ligue 1 Mercato

### Automated Transfer Tracking and Real-Time X/Twitter Notification Engine for Ligue 1

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![X](https://img.shields.io/badge/X-@Ligue__1__Mercato-000000.svg)](https://x.com/Ligue_1_Mercato)

🌐 **Langue / Language** : **Français 🇫🇷** • [English 🇬🇧](README.en.md)

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

```bash
git clone [https://github.com/delaubier/Ligue_1_Mercato.git](https://github.com/delaubier/Ligue_1_Mercato.git)
cd Ligue_1_Mercato

python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

pip install -r requirements.txt
