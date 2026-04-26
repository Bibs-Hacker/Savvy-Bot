import logging
import random
import datetime
import platform
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

import os

TOKEN = os.getenv("8654440172:AAGkb_bxr0uQ9YMA-32IhCz6w0lRXODg2QI")

logging.basicConfig(level=logging.INFO)

# ================= DATA =================
jokes = ["😂 Why do programmers hate nature? Too many bugs 🐛",
         "😂 I told my code to work... it said 'later' 😭"]

quotes = ["💬 Stay focused, stay savage 💯",
          "💬 Code. Break. Fix. Repeat 💻🔥"]

truths = ["😏 What's your biggest secret?",
          "👀 Who do you like secretly?"]

dares = ["🔥 Send a voice note saying 'I'm savage!'",
         "😅 Text your crush 'Hi 👀'"]

# ================= START =================
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🎮 Fun", callback_data='fun')],
        [InlineKeyboardButton("🛠 Tools", callback_data='tools')],
        [InlineKeyboardButton("💬 Chat", callback_data='chat')],
        [InlineKeyboardButton("⚙️ System", callback_data='system')],
    ]
    await update.message.reply_text(
        "🔥 *Savvy Bot V2 Activated* 🔥\nChoose a category:",
        parse_mode='Markdown',
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

# ================= BUTTON HANDLER =================
async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    # MAIN MENUS
    if query.data == "fun":
        keyboard = [
            [InlineKeyboardButton("😂 Joke", callback_data='joke')],
            [InlineKeyboardButton("💬 Quote", callback_data='quote')],
            [InlineKeyboardButton("🎲 Dice", callback_data='dice')],
            [InlineKeyboardButton("🎯 Guess", callback_data='guess')],
            [InlineKeyboardButton("😏 Truth", callback_data='truth')],
            [InlineKeyboardButton("🔥 Dare", callback_data='dare')],
        ]
        await query.edit_message_text("🎮 Fun Zone", reply_markup=InlineKeyboardMarkup(keyboard))

    elif query.data == "tools":
        keyboard = [
            [InlineKeyboardButton("⏰ Time", callback_data='time')],
            [InlineKeyboardButton("📅 Date", callback_data='date')],
            [InlineKeyboardButton("🌍 Info", callback_data='info')],
            [InlineKeyboardButton("🔢 Random", callback_data='random')],
            [InlineKeyboardButton("📱 Device", callback_data='device')],
        ]
        await query.edit_message_text("🛠 Tools", reply_markup=InlineKeyboardMarkup(keyboard))

    elif query.data == "chat":
        keyboard = [
            [InlineKeyboardButton("👋 Hello", callback_data='hello')],
            [InlineKeyboardButton("❤️ Love", callback_data='love')],
            [InlineKeyboardButton("🔥 Motivation", callback_data='motivate')],
            [InlineKeyboardButton("😴 Mood", callback_data='mood')],
        ]
        await query.edit_message_text("💬 Chat Mode", reply_markup=InlineKeyboardMarkup(keyboard))

    elif query.data == "system":
        keyboard = [
            [InlineKeyboardButton("📊 Status", callback_data='status')],
            [InlineKeyboardButton("⚙️ About", callback_data='about')],
        ]
        await query.edit_message_text("⚙️ System", reply_markup=InlineKeyboardMarkup(keyboard))

    # ================= FUN =================
    elif query.data == "joke":
        await query.edit_message_text(random.choice(jokes))

    elif query.data == "quote":
        await query.edit_message_text(random.choice(quotes))

    elif query.data == "dice":
        await query.message.reply_dice()

    elif query.data == "guess":
        num = random.randint(1, 10)
        await query.edit_message_text(f"🎯 Guess number: {num}")

    elif query.data == "truth":
        await query.edit_message_text(random.choice(truths))

    elif query.data == "dare":
        await query.edit_message_text(random.choice(dares))

    # ================= TOOLS =================
    elif query.data == "time":
        now = datetime.datetime.now().strftime("%H:%M:%S")
        await query.edit_message_text(f"⏰ Time: {now}")

    elif query.data == "date":
        today = datetime.date.today()
        await query.edit_message_text(f"📅 Date: {today}")

    elif query.data == "info":
        user = query.from_user
        await query.edit_message_text(f"👤 Name: {user.first_name}")

    elif query.data == "random":
        await query.edit_message_text(f"🔢 Random: {random.randint(100,999)}")

    elif query.data == "device":
        await query.edit_message_text(f"📱 System: {platform.system()}")

    # ================= CHAT =================
    elif query.data == "hello":
        await query.edit_message_text("👋 Hey bro! I'm alive 😎")

    elif query.data == "love":
        await query.edit_message_text("❤️ Love is powerful. Never play with it.")

    elif query.data == "motivate":
        await query.edit_message_text("🔥 Keep pushing. You're built different.")

    elif query.data == "mood":
        await query.edit_message_text("😴 Mood detected: Chill mode ON")

    # ================= SYSTEM =================
    elif query.data == "status":
        await query.edit_message_text("📊 Bot is running perfectly ✅")

    elif query.data == "about":
        await query.edit_message_text("🤖 Savvy Bot V2\nBuilt for vibes ⚡")

# ================= MAIN =================
def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(buttons))

    print("🔥 Savvy Bot Running...")
    app.run_polling()

if __name__ == "__main__":
    main()
