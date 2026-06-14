from telegram import Update
from telegram.ext import ContextTypes, MessageHandler, filters, ConversationHandler

from app.services.settings_service import toggle_user_notification_status, get_user_send_time, change_user_send_time
from app.keyboards.reply import get_settings_keyboard, SETTINGS_BUTTON, TOGGLE_NOTIFICATIONS_BUTTON, \
    CHANGE_SEND_TIME_BUTTON, get_main_keyboard, BACK_BUTTON, get_cancel_keyboard, CANCEL_BUTTON

WAITING_NOTIFICATION_TIME = 1


def get_handlers() -> list:
    return [
        MessageHandler(filters.Text(SETTINGS_BUTTON), settings),
        get_change_time_conversation(),
        MessageHandler(filters.Text(TOGGLE_NOTIFICATIONS_BUTTON), toggle_notifications),
        MessageHandler(filters.Text(BACK_BUTTON), back),
    ]


async def settings(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.effective_message.reply_text("Настройки", reply_markup=get_settings_keyboard())


def get_change_time_conversation() -> ConversationHandler:
    return ConversationHandler(
        entry_points=[
            MessageHandler(
                filters.Text(CHANGE_SEND_TIME_BUTTON),
                start_change_time
            ),
        ],
        states={
            WAITING_NOTIFICATION_TIME: [
                MessageHandler(
                    filters.TEXT
                    & ~filters.COMMAND
                    & ~filters.Text(CANCEL_BUTTON),
                    receive_notification_time,
                ),
            ],
        },
        fallbacks=[
            MessageHandler(
                filters.Text(CANCEL_BUTTON),
                cancel_change_time,
            ),
        ],
    )

async def start_change_time(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    notification_time = get_user_send_time(update.effective_user.id)
    await update.effective_message.reply_text(f"Текущее время отправки сообщений: {notification_time}\n"
                                              f"Чтобы изменить напишите время в формате ЧЧ:MM",
                                              reply_markup=get_cancel_keyboard())
    return WAITING_NOTIFICATION_TIME


async def receive_notification_time(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    try:
        new_time = change_user_send_time(
            update.effective_user.id,
            update.effective_message.text,
        )
    except ValueError as error:
        await update.effective_message.reply_text(str(error))
        return WAITING_NOTIFICATION_TIME

    await update.effective_message.reply_text(
        f"Время отправки изменено на {new_time}",
        reply_markup=get_settings_keyboard(),
    )
    return ConversationHandler.END


async def cancel_change_time(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.effective_message.reply_text("Настройки", reply_markup=get_settings_keyboard())
    return ConversationHandler.END


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
