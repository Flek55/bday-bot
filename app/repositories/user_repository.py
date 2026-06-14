from app.database.connection import get_connection

def create_or_update_user(
        telegram_user_id: int,
        notification_chat_id: int,
        username: str | None
):
    with get_connection() as conn:
        conn.execute("INSERT INTO users ("
                     "telegram_user_id,"
                     "notification_chat_id,"
                     "username"
                     ")"
                     "VALUES (?, ?, ?)"
                     "ON CONFLICT(telegram_user_id) DO UPDATE SET"
                     "  notification_chat_id = excluded.notification_chat_id,"
                     "  username = excluded.username",
                     (telegram_user_id, notification_chat_id, username))
