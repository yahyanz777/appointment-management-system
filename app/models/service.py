from dataclasses import dataclass


@dataclass(slots=True)
class Service:
    """Simple service data model shared through stable fields."""

    id: int | None
    name: str
    price: float
    duration_minutes: int

