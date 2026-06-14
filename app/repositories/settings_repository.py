from app.database.connection import get_connection


def get_user_status(
        telegram_user_id: int
) -> bool | None:
    with get_connection() as conn:
        row = conn.execute("SELECT is_active "
                           "FROM users "
                           "WHERE telegram_user_id = ?",
                           (telegram_user_id,)).fetchone()

        if row is None:
            return None

        return bool(row["is_active"])


def update_user_active_status(
        telegram_user_id: int,
        status: bool
) -> None:
    with get_connection() as conn:
        conn.execute("UPDATE users "
                     "SET is_active = ? "
                     "WHERE telegram_user_id = ?",
                     (status, telegram_user_id))


def get_user_notification_time(
        telegram_user_id: int
) -> str | None:
    with get_connection() as conn:
        row = conn.execute("SELECT notification_time "
                           "FROM users "
                           "WHERE telegram_user_id = ?",
                           (telegram_user_id,)).fetchone()
        if row is None:
            return None

        return row["notification_time"]


def update_user_notification_time(
        telegram_user_id: int,
        time: str
) -> bool:
    with get_connection() as conn:
        cursor = conn.execute("UPDATE users "
                              "SET notification_time = ? "
                              "WHERE telegram_user_id = ?",
                              (time, telegram_user_id))
        return cursor.rowcount > 0
