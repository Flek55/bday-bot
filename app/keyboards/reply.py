from telegram import ReplyKeyboardMarkup, KeyboardButton

PEOPLE_BUTTON = "Люди"
BIRTHDAYS_BUTTON = "Дни рождения"
SETTINGS_BUTTON = "Настройки"
HELP_BUTTON = "Помощь"
BACK_BUTTON = "Назад"
CANCEL_BUTTON = "Отмена"


def get_main_keyboard() -> ReplyKeyboardMarkup:
    keyboard = [
        [
            KeyboardButton(PEOPLE_BUTTON),
            KeyboardButton(BIRTHDAYS_BUTTON)
        ],
        [
            KeyboardButton(SETTINGS_BUTTON),
            KeyboardButton(HELP_BUTTON)
        ]
    ]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True, is_persistent=True)


def get_people_keyboard() -> ReplyKeyboardMarkup:
    keyboard = [
        [
            KeyboardButton()
        ],
        [
            KeyboardButton(BACK_BUTTON)
        ]
    ]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True, is_persistent=True)


def get_birthdays_keyboard() -> ReplyKeyboardMarkup:
    keyboard = [
        [
            KeyboardButton()
        ],
        [
            KeyboardButton(BACK_BUTTON)
        ]
    ]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True, is_persistent=True)


def get_settings_keyboard() -> ReplyKeyboardMarkup:
    keyboard = [
        [
            KeyboardButton()
        ],
        [
            KeyboardButton(BACK_BUTTON)
        ]
    ]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True, is_persistent=True)
