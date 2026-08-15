from app.models.customer import Customer
from app.file_handlers.customer_file_handler import CustomerFileHandler


class CustomerService:
    """Public interface for customer management use cases."""

    def __init__(self, file_handler: CustomerFileHandler) -> None:
        self._file_handler = file_handler

    def validate_customer_data(self, name: str, phone: str, email: str) -> None:
        """Validates customer input fields."""
        if not name or not name.strip():
            raise ValueError("Customer name cannot be empty.")
        if not phone or not phone.strip():
            raise ValueError("Phone number cannot be empty.")
        if not email or "@" not in email or "." not in email:
            raise ValueError("Invalid email address formatting.")

    def create_customer(self, name: str, phone: str, email: str) -> int:
        """Validate and create a customer."""
        self.validate_customer_data(name, phone, email)
        customer = Customer(
            id=None,
            name=name.strip(),
            phone=phone.strip(),
            email=email.strip(),
        )
        return self._file_handler.add(customer)

    def get_customer(self, customer_id: int) -> Customer | None:
        """Return customer details for other layers."""
        return self._file_handler.get_by_id(customer_id)

    def list_customers(self) -> list[Customer]:
        """Return all registered customers."""
        return self._file_handler.list_all()

    def update_customer(
        self,
        customer_id: int,
        name: str | None = None,
        phone: str | None = None,
        email: str | None = None,
    ) -> bool:
        """Validate and update an existing customer record."""
        existing = self._file_handler.get_by_id(customer_id)
        if existing is None:
            return False

        updated_name = name if name is not None else existing.name
        updated_phone = phone if phone is not None else existing.phone
        updated_email = email if email is not None else existing.email

        self.validate_customer_data(updated_name, updated_phone, updated_email)

        updated_customer = Customer(
            id=customer_id,
            name=updated_name.strip(),
            phone=updated_phone.strip(),
            email=updated_email.strip(),
        )
        self._file_handler.update(updated_customer)
        return True

    def delete_customer(self, customer_id: int) -> bool:
        """Delete a customer by ID."""
        existing = self._file_handler.get_by_id(customer_id)
        if existing is None:
            return False
        self._file_handler.delete(customer_id)
        return True