from lib2to3.fixer_util import Comma

from telegram import Update
from telegram.ext import ContextTypes, CommandHandler

from app.services.common_service import create_user

def get_handlers():
    return [
        CommandHandler("start", start),
        CommandHandler("help", help)
    ]


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    telegram_user, chat = update.effective_user, update.effective_chat
    create_user(telegram_user.id, chat.id, telegram_user.username)
    await update.message.reply_text("Вы зарегистрированы!")

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Бот помогает с напоминаниями о днях рождения")

async def cancel():
    pass
