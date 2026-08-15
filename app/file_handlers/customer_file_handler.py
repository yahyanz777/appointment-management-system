from pathlib import Path

from app.models.customer import Customer


class CustomerFileHandler:
    """Handles customer records stored in a text file."""

    def __init__(self, file_path: Path) -> None:
        self._file_path = file_path

    def add(self, customer: Customer) -> int:
        """Add a customer to the customer file and return its new ID."""
        customers = self.list_all()
        next_id = max((c.id for c in customers if c.id is not None), default=0) + 1

        customer.id = next_id
        # Ensure parent directory exists
        self._file_path.parent.mkdir(parents=True, exist_ok=True)
        with open(self._file_path, "a") as f:
            f.write(customer.to_file_line())

        return next_id

    def get_by_id(self, customer_id: int) -> Customer | None:
        """Read a customer by ID from the customer file."""
        for customer in self.list_all():
            if customer.id == customer_id:
                return customer
        return None

    def list_all(self) -> list[Customer]:
        """Read all customers from the customer file."""
        if not self._file_path.exists():
            return []

        customers = []
        with open(self._file_path, "r") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                customer = Customer.from_file_line(line)
                if customer is not None:
                    customers.append(customer)
        return customers

    def update(self, customer: Customer) -> None:
        """Update an existing customer in the customer file."""
        customers = self.list_all()
        updated = False

        for i, existing in enumerate(customers):
            if existing.id == customer.id:
                customers[i] = customer
                updated = True
                break

        if not updated:
            raise ValueError(f"No customer found with id {customer.id}")

        self._write_all(customers)

    def delete(self, customer_id: int) -> None:
        """Delete a customer by ID from the customer file."""
        customers = self.list_all()
        remaining = [c for c in customers if c.id != customer_id]

        if len(remaining) == len(customers):
            raise ValueError(f"No customer found with id {customer_id}")

        self._write_all(remaining)

    def _write_all(self, customers: list[Customer]) -> None:
        # Ensure parent directory exists
        self._file_path.parent.mkdir(parents=True, exist_ok=True)
        with open(self._file_path, "w") as f:
            for customer in customers:
                f.write(customer.to_file_line())

