from telegram import Update
from telegram.ext import ContextTypes, MessageHandler, filters

from app.services.settings_service import toggle_user_notification_status, get_user_send_time
from app.keyboards.reply import get_settings_keyboard, SETTINGS_BUTTON, TOGGLE_NOTIFICATIONS_BUTTON, \
    CHANGE_SEND_TIME_BUTTON, get_main_keyboard, BACK_BUTTON, get_cancel_keyboard, CANCEL_BUTTON


def get_handlers() -> list:
    return [
        MessageHandler(filters.Text(SETTINGS_BUTTON), settings),
        MessageHandler(filters.Text(CHANGE_SEND_TIME_BUTTON), time),
        MessageHandler(filters.Text(TOGGLE_NOTIFICATIONS_BUTTON), toggle_notifications),
        MessageHandler(filters.Text(BACK_BUTTON), back),
        MessageHandler(filters.Text(CHANGE_SEND_TIME_BUTTON), time),
        MessageHandler(filters.Text(CANCEL_BUTTON), cancel)
    ]


async def settings(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.effective_message.reply_text("Настройки", reply_markup=get_settings_keyboard())


async def time(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    notification_time = get_user_send_time(update.effective_user.id)
    await update.effective_message.reply_text(f"Текущее время отправки сообщений: {notification_time}\n"
                                              f"Чтобы изменить напишите время в формате ЧЧ:MM",
                                              reply_markup=get_cancel_keyboard())


async def toggle_notifications(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    telegram_user = update.effective_user.id
    status = toggle_user_notification_status(telegram_user)
    if status:
        await update.effective_message.reply_text("Теперь вы будете получать уведомления",
                                                  reply_markup=get_settings_keyboard())
    else:
        await update.effective_message.reply_text("Вы отказались от уведомлений",
                                                  reply_markup=get_settings_keyboard())


async def back(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.effective_message.reply_text("Главное меню", reply_markup=get_main_keyboard())


async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.effective_message.reply_text("Настройки", reply_markup=get_settings_keyboard())
