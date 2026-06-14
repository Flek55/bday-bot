PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    telegram_user_id INTEGER NOT NULL UNIQUE,
    notification_chat_id INTEGER NOT NULL,
    username TEXT,
    timezone TEXT NOT NULL DEFAULT 'Europe/Moscow',
    notification_time TEXT NOT NULL DEFAULT '09:00',
    is_active INTEGER NOT NULL DEFAULT 1
        CHECK (is_active IN (0, 1)),
    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS people (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    full_name TEXT NOT NULL,

    birth_day INTEGER NOT NULL
        CHECK (birth_day BETWEEN 1 AND 31),

    birth_month INTEGER NOT NULL
        CHECK (birth_month BETWEEN 1 AND 12),

    birth_year INTEGER,
    notes TEXT,
    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (user_id)
        REFERENCES users(id)
        ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS notification_log (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    person_id INTEGER,

    notification_type TEXT NOT NULL
        CHECK (
            notification_type IN (
                'day_before',
                'birthday',
                'weekly'
            )
        ),

    birthday_date TEXT,
    period_start TEXT,
    sent_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (user_id)
        REFERENCES users(id)
        ON DELETE CASCADE,

    FOREIGN KEY (person_id)
        REFERENCES people(id)
        ON DELETE CASCADE
);

CREATE INDEX IF NOT EXISTS idx_people_user
ON people(user_id);

CREATE INDEX IF NOT EXISTS idx_people_user_birthday
ON people(user_id, birth_month, birth_day);

CREATE UNIQUE INDEX IF NOT EXISTS unique_person_notification
ON notification_log(
    person_id,
    notification_type,
    birthday_date
)
WHERE person_id IS NOT NULL;

CREATE UNIQUE INDEX IF NOT EXISTS unique_weekly_notification
ON notification_log(
    user_id,
    notification_type,
    period_start
)
WHERE notification_type = 'weekly';
