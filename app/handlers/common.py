from telegram import Update
from telegram.ext import ContextTypes

from app.repositories.user_repository import create_or_update_user


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    telegram_user, chat = update.effective_user, update.effective_chat
    create_or_update_user(telegram_user.id, chat.id, telegram_user.username)
    await update.message.reply_text("Вы зарегистрированы!")
