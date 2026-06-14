from os import getenv

from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

from app.handlers.common import start

load_dotenv()
bot_token = getenv("BOT_TOKEN")

if bot_token is None:
    raise RuntimeError("BOT_TOKEN is not set")

app = ApplicationBuilder().token(bot_token).build()
app.add_handler(CommandHandler("start", start))


app.run_polling()
