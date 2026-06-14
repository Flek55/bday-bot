from telegram import Update
from telegram.ext import ContextTypes, MessageHandler, filters

from app.keyboards.reply import get_people_keyboard, BIRTHDAYS_BUTTON


def get_handlers() -> list:
    return [
        MessageHandler(filters.Text(BIRTHDAYS_BUTTON), people_page),
    ]

async def people_page(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.effective_message.reply_text("Дни рождения", reply_markup=get_people_keyboard())

async def add_person(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    telegram_user = update.effective_user

async def list_people(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    pass

async def delete_person(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    pass
