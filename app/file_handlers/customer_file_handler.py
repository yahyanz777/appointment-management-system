from pathlib import Path

from app.models.customer import Customer


class CustomerFileHandler:
    """Handles customer records stored in a text file."""

    def __init__(self, file_path: Path) -> None:
        self._file_path = file_path

    def add(self, customer: Customer) -> int:
        """Add a customer to the customer file and return its new ID."""
        raise NotImplementedError("TODO: implement customer creation")

    def get_by_id(self, customer_id: int) -> Customer | None:
        """Read a customer by ID from the customer file."""
        raise NotImplementedError("TODO: implement customer lookup")

    def list_all(self) -> list[Customer]:
        """Read all customers from the customer file."""
        raise NotImplementedError("TODO: implement customer listing")

    def update(self, customer: Customer) -> None:
        """Update an existing customer in the customer file."""
        raise NotImplementedError("TODO: implement customer update")

    def delete(self, customer_id: int) -> None:
        """Delete a customer by ID from the customer file."""
        raise NotImplementedError("TODO: implement customer deletion")

