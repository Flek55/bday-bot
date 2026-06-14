from datetime import datetime

from app.repositories.settings_repository import update_user_active_status, get_user_status, get_user_notification_time, \
    update_user_notification_time


def toggle_user_notification_status(
        telegram_user_id: int,
) -> bool:
    status = get_user_status(telegram_user_id)

    if status is None:
        raise ValueError("User is not registered")

    new_status = not status
    update_user_active_status(telegram_user_id, new_status)

    return new_status


def get_user_send_time(
        telegram_user_id: int
) -> str:
    time = get_user_notification_time(telegram_user_id)

    if time is None:
        raise ValueError("User is not registered")

    return time


def change_user_send_time(
        telegram_user_id: int,
        time: str
) -> str:
    try:
        parsed_time = datetime.strptime(time.strip(), "%H:%M")
        normalized_time = parsed_time.strftime("%H:%M")
    except ValueError as error:
        raise ValueError("Вводите время в формате ЧЧ:ММ") from error

    updated = update_user_notification_time(telegram_user_id, normalized_time)

    if not updated:
        raise ValueError("Пользователь не зарегистрирован")

    return normalized_time
