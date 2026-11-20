# 🇨🇿 Czech–Amharic Learning Bot 🇪🇹

An interactive Telegram bot designed to help Amharic speakers learn everyday Czech language phrases easily through flashcards, pronunciation guides in Amharic script (Fidel), and instant audio pronunciation.

---

## ✨ Features

- 🗂️ **Categorized Flashcards**: Explore essential phrases across various topics (Greetings, Travel, Numbers, Emergency, etc.).
- 🗣️ **Amharic Phonetics**: Czech pronunciation transcribed into Amharic script so you can read and pronounce words accurately.
- 🔊 **Voice Audio Pronunciation**: Built-in text-to-speech (gTTS) delivers clear Czech native voice messages with one tap.
- 📱 **Interactive UI**: Navigate easily with inline buttons (`Prev`, `Next`, `Listen`, and `All Categories`).
- 🇬🇧 **Trilingual Context**: Every flashcard shows the phrase in **Czech**, **Amharic**, and **English**.

---

## 📸 Preview

```text
📂 Greetings & Basics (1/12)
━━━━━━━━━━━━━━━━━━
🇨🇿 Czech: Dobrý den
🗣️ Pronunciation: ዶብሪ ደን
🇪🇹 Amharic: ጤና ይስጥልኝ / እንደምን ዋሉ
🇬🇧 English: Hello / Good day (Formal)

[ 🔊 Listen (Czech Audio) ]
[ ⬅️ Prev ] [ Next ➡️ ]
[ 🏠 All Categories ]
```

---

## 📁 Project Structure

```text
czech_amharic_bot/
├── bot.py             # Main Telegram bot logic and handlers
├── lessons.json       # Trilingual vocabulary and phrases database
├── .env.example       # Template for environment variables
├── .env               # Your local bot token (ignored by Git)
├── .gitignore         # Ignores sensitive and temporary files
└── README.md          # Project documentation
```

---

## 🚀 Getting Started

### 1. Prerequisites
- Python 3.9+ installed on your machine.
- A Telegram Bot Token from [@BotFather](https://t.me/BotFather).

### 2. Clone the Repository
```bash
git clone https://github.com/your-username/czech-amharic-bot.git
cd czech-amharic-bot
```

### 3. Create and Activate a Virtual Environment
- **Windows (PowerShell):**
  ```powershell
  python -m venv venv
  .\venv\Scripts\Activate.ps1
  ```
- **macOS / Linux:**
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

### 4. Install Dependencies
```bash
pip install python-telegram-bot gTTS python-dotenv
```

### 5. Configure Environment Variables
Copy `.env.example` to `.env`:
- **Windows:**
  ```powershell
  copy .env.example .env
  ```
- **macOS / Linux:**
  ```bash
  cp .env.example .env
  ```

Open `.env` and insert your Telegram bot token:
```env
BOT_TOKEN=your_telegram_bot_token_here
```

### 6. Run the Bot
```bash
python bot.py
```

Now open Telegram, search for your bot, and send `/start` to begin learning!

---

## 🛠️ Tech Stack

- **[python-telegram-bot](https://python-telegram-bot.org/)** – Telegram Bot API wrapper
- **[gTTS (Google Text-to-Speech)](https://pypi.org/project/gTTS/)** – On-the-fly Czech audio generation
- **[python-dotenv](https://pypi.org/project/python-dotenv/)** – Environment variable management

---

## 📄 License

This project is licensed under the MIT License — feel free to use and adapt it!
