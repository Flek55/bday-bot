from app.repositories.settings_repository import update_user_active_status, get_user_status


def toggle_user_notification_status(
        telegram_user_id: int,
) -> bool:
    status = get_user_status(telegram_user_id)

    if status is None:
        raise ValueError("User is not registered")

    new_status = not status
    update_user_active_status(telegram_user_id, new_status)

    return new_status
