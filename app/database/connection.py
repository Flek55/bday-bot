import sqlite3
from collections.abc import Iterator
from contextlib import contextmanager
from pathlib import Path

DB_PATH = Path(__file__).resolve().parents[2] / "data" / "birthdays.db"
SCHEMA_PATH = Path(__file__).with_name("schema.sql")


def initialize_database() -> None:
    if not DB_PATH.exists():
        DB_PATH.parent.mkdir(parents=True, exist_ok=True)
        schema = SCHEMA_PATH.read_text(encoding="utf-8")

        with get_connection() as connection:
            connection.executescript(schema)


@contextmanager
def get_connection() -> Iterator[sqlite3.Connection]:
    connection = sqlite3.connect(DB_PATH)

    try:
        connection.row_factory = sqlite3.Row
        connection.execute("PRAGMA foreign_keys = ON")

        with connection:
            yield connection
    finally:
        connection.close()
