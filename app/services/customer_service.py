from app.models.customer import Customer
from app.file_handlers.customer_file_handler import CustomerFileHandler


class CustomerService:
    """Public interface for customer management use cases."""

    def __init__(self, file_handler: CustomerFileHandler) -> None:
        self._file_handler = file_handler

    def create_customer(self, name: str, phone: str, email: str) -> int:
        """Validate and create a customer."""
        # TODO: add customer validation rules.
        customer = Customer(id=None, name=name, phone=phone, email=email)
        return self._file_handler.add(customer)

    def get_customer(self, customer_id: int) -> Customer | None:
        """Return customer details for other layers."""
        return self._file_handler.get_by_id(customer_id)
