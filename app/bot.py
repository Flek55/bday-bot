from os import getenv

from dotenv import load_dotenv
from telegram.ext import ApplicationBuilder

from app.database.connection import initialize_database
from app.handlers import birthdays, common, people, settings


def main() -> None:
    load_dotenv()
    initialize_database()

    bot_token = getenv("BOT_TOKEN")

    if bot_token is None:
        raise RuntimeError("BOT_TOKEN is not set")

    app = ApplicationBuilder().token(bot_token).build()
    # common handlers
    for handler in common.get_handlers():
        app.add_handler(handler)
    # settings
    for handler in settings.get_handlers():
        app.add_handler(handler)
    # people
    for handler in people.get_handlers():
        app.add_handler(handler)
    app.run_polling()


if __name__ == "__main__":
    main()
