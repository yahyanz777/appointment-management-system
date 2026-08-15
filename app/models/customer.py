from dataclasses import dataclass


@dataclass(slots=True)
class Customer:
    """Simple customer data model shared through stable fields."""

    id: int | None
    name: str
    phone: str
    email: str

    def to_file_line(self) -> str:
        """Converts object attributes into a pipe-separated string for text storage."""
        id_str = str(self.id) if self.id is not None else ""
        return f"{id_str}|{self.name}|{self.phone}|{self.email}\n"

    @classmethod
    def from_file_line(cls, line: str) -> "Customer | None":
        """Creates a Customer instance from a pipe-separated line."""
        parts = line.strip().split("|")
        if len(parts) == 4:
            raw_id, name, phone, email = parts
            customer_id = int(raw_id) if raw_id.isdigit() else None
            return cls(id=customer_id, name=name, phone=phone, email=email)
        return None

    def to_dict(self) -> dict:
        """Returns customer properties as a dictionary."""
        return {
            "id": self.id,
            "name": self.name,
            "phone": self.phone,
            "email": self.email,
        }

