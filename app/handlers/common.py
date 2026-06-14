from telegram import Update
from telegram.ext import ContextTypes, CommandHandler, MessageHandler, filters

from app.keyboards.reply import HELP_BUTTON, get_main_keyboard, MAIN_MENU_BUTTON
from app.services.common_service import create_user
from app.keyboards import reply, inline


def get_handlers() -> list:
    return [
        CommandHandler("start", start),
        CommandHandler("help", help),
        MessageHandler(filters.Text(HELP_BUTTON), help),
        MessageHandler(filters.Text(MAIN_MENU_BUTTON), main_menu),
    ]


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    telegram_user, chat = update.effective_user, update.effective_chat
    create_user(telegram_user.id, chat.id, telegram_user.username)
    await update.effective_message.reply_text("Вы зарегистрированы!",
                                              reply_markup=reply.get_main_keyboard())


async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.effective_message.reply_text("Бот помогает с напоминаниями о днях рождения")

async def main_menu(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.effective_message.reply_text("Главное меню", reply_markup=get_main_keyboard())