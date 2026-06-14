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
