from app.models.service import Service
from app.file_handlers.service_file_handler import ServiceFileHandler


class ServiceService:
    """Public interface for service management use cases."""

    def __init__(self, file_handler: ServiceFileHandler) -> None:
        self._file_handler = file_handler

    def create_service(self, name: str, price: float, duration_minutes: int) -> int:
        """Validate and create a service."""
        # TODO: add service validation rules.
        service = Service(
            id=None,
            name=name,
            price=price,
            duration_minutes=duration_minutes,
        )
        return self._file_handler.add(service)

    def get_service(self, service_id: int) -> Service | None:
        """Return service details for other layers."""
        return self._file_handler.get_by_id(service_id)
