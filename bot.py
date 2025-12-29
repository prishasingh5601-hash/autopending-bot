from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "7840614765:AAEIRxT-TnITvteBPq1SvTM_jyDAQs7jfz4"

CHANNELS = [
    ("Cinema Hub 🎬", "https://t.me/movies_3_1"),
    ("Masala Video 🔥", "https://t.me/+UjbqOeyUwo"),
    ("Movies Upload 🍿", "https://t.me/+SRCkRXXXX"),
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    buttons = []
    for name, url in CHANNELS:
        buttons.append([InlineKeyboardButton(name, url=url)])

    reply_markup = InlineKeyboardMarkup(buttons)

    await update.message.reply_text(
        "🖼 Our All Channel List 🖼\n\n👇 All Channel Join Now 👇",
        reply_markup=reply_markup
    )

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.run_polling()
