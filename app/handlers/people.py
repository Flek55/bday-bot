from telegram import Update
from telegram.ext import ContextTypes


async def add(update: Update) -> None:
    telegram_user = update.effective_user

async def list():
    pass

async def delete():
    pass
