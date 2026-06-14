from dataclasses import dataclass

@dataclass(frozen=True)
class PersonInput:
    full_name: str
    birth_day: int
    birth_month: int
    birth_year: int | None
    notes: str | None