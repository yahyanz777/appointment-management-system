from app.models.service import Service
from app.file_handlers.service_file_handler import ServiceFileHandler


class ServiceService:
    """Public interface for service management use cases."""

    def __init__(self, file_handler: ServiceFileHandler) -> None:
        self._file_handler = file_handler

    def create_service(self, name: str, price: float, duration_minutes: int) -> int:
        """Validate and create a service."""
        self._validate(name, price, duration_minutes)

        service = Service(
            id=None,
            name=name.strip(),
            price=float(price),
            duration_minutes=int(duration_minutes),
        )
        return self._file_handler.add(service)

    def get_service(self, service_id: int) -> Service | None:
        """Return service details for other layers."""
        return self._file_handler.get_by_id(service_id)

    def list_services(self) -> list[Service]:
        """Return all services."""
        return self._file_handler.list_all()

    def update_service(
        self,
        service_id: int,
        name: str | None = None,
        price: float | None = None,
        duration_minutes: int | None = None,
    ) -> None:
        """Update an existing service, keeping any omitted fields unchanged."""
        existing = self._file_handler.get_by_id(service_id)
        if existing is None:
            raise ValueError(f"No service found with id {service_id}")

        new_name = name if name is not None else existing.name
        new_price = price if price is not None else existing.price
        new_duration = duration_minutes if duration_minutes is not None else existing.duration_minutes

        self._validate(new_name, new_price, new_duration)

        existing.name = new_name.strip()
        existing.price = float(new_price)
        existing.duration_minutes = int(new_duration)

        self._file_handler.update(existing)

    def delete_service(self, service_id: int) -> None:
        """Delete a service by ID."""
        self._file_handler.delete(service_id)

    # ---------- validation ----------

    @staticmethod
    def _validate(name: str, price: float, duration_minutes: int) -> None:
        if not name or not str(name).strip():
            raise ValueError("Service name cannot be empty.")

        try:
            price = float(price)
        except (TypeError, ValueError):
            raise ValueError("Price must be a number.")
        if price < 0:
            raise ValueError("Price cannot be negative.")

        try:
            duration_minutes = int(duration_minutes)
        except (TypeError, ValueError):
            raise ValueError("Duration must be a whole number of minutes.")
        if duration_minutes <= 0:
            raise ValueError("Duration must be greater than zero.")