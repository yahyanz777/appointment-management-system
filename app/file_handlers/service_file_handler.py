from pathlib import Path

from app.models.service import Service


class ServiceFileHandler:
    """Handles service records stored in a text file."""

    def __init__(self, file_path: Path) -> None:
        self._file_path = file_path

    def add(self, service: Service) -> int:
        """Add a service to the service file and return its new ID."""
        raise NotImplementedError("TODO: implement service creation")

    def get_by_id(self, service_id: int) -> Service | None:
        """Read a service by ID from the service file."""
        raise NotImplementedError("TODO: implement service lookup")

    def list_all(self) -> list[Service]:
        """Read all services from the service file."""
        raise NotImplementedError("TODO: implement service listing")

    def update(self, service: Service) -> None:
        """Update an existing service in the service file."""
        raise NotImplementedError("TODO: implement service update")

    def delete(self, service_id: int) -> None:
        """Delete a service by ID from the service file."""
        raise NotImplementedError("TODO: implement service deletion")

