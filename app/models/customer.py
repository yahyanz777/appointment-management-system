from dataclasses import dataclass


@dataclass(slots=True)
class Customer:
    """Simple customer data model shared through stable fields."""

    id: int | None
    name: str
    phone: str
    email: str

