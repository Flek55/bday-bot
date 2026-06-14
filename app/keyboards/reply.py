from telegram import ReplyKeyboardMarkup, KeyboardButton

BIRTHDAYS_BUTTON = "Дни рождения"
SETTINGS_BUTTON = "Настройки"
HELP_BUTTON = "Помощь"
BACK_BUTTON = "Назад"
CANCEL_BUTTON = "Отмена"

LIST_BIRTHDAYS_BUTTON = "Просмотреть дни рождения"
ADD_BIRTHDAY_BUTTON = "Добавить день рождения"

CHANGE_SEND_TIME_BUTTON = "Изменить время отправки"
TOGGLE_NOTIFICATIONS_BUTTON = "Вкл/Выкл уведомления"


def get_main_keyboard() -> ReplyKeyboardMarkup:
    keyboard = [
        [
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
            KeyboardButton(ADD_BIRTHDAY_BUTTON),
            KeyboardButton(LIST_BIRTHDAYS_BUTTON)
        ],
        [
            KeyboardButton(BACK_BUTTON)
        ]
    ]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True, is_persistent=True)


def get_settings_keyboard() -> ReplyKeyboardMarkup:
    keyboard = [
        [
            KeyboardButton(CHANGE_SEND_TIME_BUTTON),
            KeyboardButton(TOGGLE_NOTIFICATIONS_BUTTON)
        ],
        [
            KeyboardButton(BACK_BUTTON)
        ]
    ]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True, is_persistent=True)
