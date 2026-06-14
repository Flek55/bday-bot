from app.repositories.user_repository import create_or_update_user

def create_user(telegram_user_id: int, notification_chat_id: int, username: str | None):
    create_or_update_user(telegram_user_id, notification_chat_id, username)
