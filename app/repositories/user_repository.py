import sqlite3

from app.database.connection import get_connection


def create_or_update_user(
        telegram_user_id: int,
        notification_chat_id: int,
        username: str | None
) -> None:
    with get_connection() as conn:
        return conn.execute("INSERT INTO users ("
                            "telegram_user_id,"
                            "notification_chat_id,"
                            "username"
                            ")"
                            "VALUES (?, ?, ?)"
                            "ON CONFLICT(telegram_user_id) DO UPDATE SET"
                            "  notification_chat_id = excluded.notification_chat_id,"
                            "  username = excluded.username",
                            (telegram_user_id, notification_chat_id, username))


def toggle_user_status(
        telegram_user_id: int,
        is_active: bool
) -> None:
    with get_connection() as conn:
        conn.execute("UPDATE users "
                     "SET is_active = ? "
                     "WHERE telegram_user_id = ? ",
                     (is_active, telegram_user_id))


def get_user_by_telegram_id(
        telegram_user_id: int
) -> sqlite3.Row | None:
    with get_connection() as conn:
        return conn.execute("SELECT * "
                            "FROM users "
                            "WHERE telegram_user_id = ?",
                            (telegram_user_id,)).fetchone()
