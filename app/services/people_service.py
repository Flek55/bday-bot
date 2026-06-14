from datetime import datetime

from app.models.person import PersonInput
from app.repositories.people_repository import create_person
from app.repositories.user_repository import get_user_by_telegram_id

YEAR_DATE = 2
DAY = 0
MONTH = 1
YEAR = 2


def parse_birthday(value: str) -> tuple[int, int, int | None]:
    value = value.strip()

    formats = (
        ("%d.%m.%Y", True),
        ("%d.%m", False),
    )

    for date_format, has_year in formats:
        try:
            if has_year:
                parsed_date = datetime.strptime(value, date_format)
            else:
                parsed_date = datetime.strptime(
                    f"{value}.2000",
                    "%d.%m.%Y",
                )

            birth_year = parsed_date.year if has_year else None

            return (
                parsed_date.day,
                parsed_date.month,
                parsed_date.year,
            )
        except ValueError:
            continue
    raise ValueError(
        "Неверная дата"
    )


def create_person_input(
        full_name: str,
        birthday: str,
        notes: str | None,
) -> PersonInput:
    try:
        birth_date = parse_birthday(birthday)

        if len(full_name) == 0 or len(full_name) > 100:
            raise ValueError("Некоректная длина имени")

        if birth_date[YEAR] > datetime.now().year:
            raise ValueError("Год в будущем")

        if notes == "":
            notes = None

        return PersonInput(
            full_name=full_name,
            birth_day=birth_date[DAY],
            birth_month=birth_date[MONTH],
            birth_year=birth_date[YEAR],
            notes=notes,
        )
    except ValueError as error:
        raise error


def add_person(
        telegram_user_id: int,
        person: PersonInput,
) -> int:
    user = get_user_by_telegram_id(telegram_user_id)
    if user is None:
        raise ValueError("Пользователь не зарегистрирован")
    return create_person(
        user["id"],
        person.full_name,
        day=person.birth_day,
        month=person.birth_month,
        year=person.birth_year,
        notes=person.notes,
    )
