import json
import os
from io import BytesIO
# pyrefly: ignore[missing-import]
from dotenv import load_dotenv
# pyrefly: ignore[missing-import]
from gtts import gTTS
# pyrefly: ignore[missing-import]
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
# pyrefly: ignore[missing-import]
from telegram.ext import (
    Application,
    CallbackQueryHandler,
    CommandHandler,
    ContextTypes,
)

# Load environment variables from .env file
load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN is not set. Please set it in your .env file.")

# Load lessons from JSON (Ensure UTF-8 encoding for Amharic & Czech characters)
with open("lessons.json", "r", encoding="utf-8") as f:
    LESSONS = json.load(f)

CATEGORIES = list(LESSONS.keys())


def build_category_menu() -> InlineKeyboardMarkup:
    """Creates the main menu with one button per category."""
    keyboard = [
        [InlineKeyboardButton(f"📚 {cat} ({len(LESSONS[cat])})", callback_data=f"cat:{i}:0")]
        for i, cat in enumerate(CATEGORIES)
    ]
    return InlineKeyboardMarkup(keyboard)


def format_card(cat_idx: int, card_idx: int):
    """Formats the flashcard text and navigation buttons."""
    category_name = CATEGORIES[cat_idx]
    phrases = LESSONS[category_name]
    total = len(phrases)
    item = phrases[card_idx]

    text = (
        f"📂 *{category_name}* ({card_idx + 1}/{total})\n"
        f"━━━━━━━━━━━━━━━━━━\n"
        f"🇨🇿 *Czech:* `{item['cz']}`\n"
        f"🗣️ *Pronunciation:* {item['phonetic']}\n"
        f"🇪🇹 *Amharic:* {item['am']}\n"
        f"🇬🇧 *English:* _{item['en']}_"
    )

    # Navigation buttons
    nav_row = []
    if card_idx > 0:
        nav_row.append(InlineKeyboardButton("⬅️ Prev", callback_data=f"cat:{cat_idx}:{card_idx - 1}"))
    if card_idx < total - 1:
        nav_row.append(InlineKeyboardButton("Next ➡️", callback_data=f"cat:{cat_idx}:{card_idx + 1}"))

    keyboard = [
        [InlineKeyboardButton("🔊 Listen (Czech Audio)", callback_data=f"audio:{cat_idx}:{card_idx}")],
        nav_row,
        [InlineKeyboardButton("🏠 All Categories", callback_data="menu")],
    ]
    # Filter out empty rows (e.g., if nav_row is empty on a 1-card category)
    keyboard = [row for row in keyboard if row]

    return text, InlineKeyboardMarkup(keyboard)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handles the /start command."""
    welcome_text = (
        "🇪🇹 *እንኳን ደህና መጡ!* | 🇨🇿 *Vítejte!*\n\n"
        "Welcome to the **Czech–Amharic Learning Bot**.\n"
        "Choose a category below to start practicing essential phrases:"
    )
    await update.message.reply_text(
        welcome_text,
        reply_markup=build_category_menu(),
        parse_mode="Markdown",
    )


async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handles all inline button clicks."""
    query = update.callback_query
    await query.answer()  # Removes the loading spinner on the button
    data = query.data

    if data == "menu":
        await query.edit_message_text(
            "📚 *Select a category:*",
            reply_markup=build_category_menu(),
            parse_mode="Markdown",
        )

    elif data.startswith("cat:"):
        _, cat_idx, card_idx = data.split(":")
        text, markup = format_card(int(cat_idx), int(card_idx))
        await query.edit_message_text(text, reply_markup=markup, parse_mode="Markdown")

    elif data.startswith("audio:"):
        _, cat_idx, card_idx = data.split(":")
        category_name = CATEGORIES[int(cat_idx)]
        czech_phrase = LESSONS[category_name][int(card_idx)]["cz"]

        # Generate Czech audio in memory without cluttering disk
        tts = gTTS(text=czech_phrase, lang="cs", slow=False)
        audio_buffer = BytesIO()
        tts.write_to_fp(audio_buffer)
        audio_buffer.seek(0)

        await query.message.reply_voice(
            voice=audio_buffer,
            caption=f"🔊 {czech_phrase}",
        )


def main() -> None:
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))

    print("Bot is running...")
    app.run_polling()


if __name__ == "__main__":
    main()