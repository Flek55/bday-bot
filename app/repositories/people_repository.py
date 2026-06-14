from app.database.connection import get_connection


def create_person(
        user_id: int,
        full_name: str,
        day: int,
        month: int,
        year: int | None,
        notes: str | None
) -> int:
    with get_connection() as conn:
        cursor = conn.execute("INSERT INTO people ("
                     "user_id,"
                     "full_name,"
                     "birth_day,"
                     "birth_month,"
                     "birth_year,"
                     "notes"
                     ")"
                     "VALUES (?, ?, ?, ?, ?, ?)",
                     (user_id, full_name, day, month, year, notes))
        return cursor.lastrowid

def get_people(user_id: int):
    with get_connection() as conn:
        return conn.execute("SELECT * FROM people "
                     "WHERE user_id = ?", (user_id,)).fetchall()

def get_person(user_id: int, person_id: int):
    with get_connection() as conn:
        return conn.execute("SELECT * FROM people "
                              "WHERE id = ? AND user_id = ?", (person_id, user_id)).fetchone()

def delete_person(user_id: int, person_id: int) -> bool:
    with get_connection() as conn:
        cursor = conn.execute("DELETE FROM people "
                     "WHERE id = ? AND user_id = ?", (person_id, user_id))
        return cursor.rowcount > 0