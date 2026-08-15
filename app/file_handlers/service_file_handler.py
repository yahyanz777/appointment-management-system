from pathlib import Path

from app.models.service import Service


class ServiceFileHandler:
    """Handles service records stored in a text file."""

    def __init__(self, file_path: Path) -> None:
        self._file_path = file_path

    def add(self, service: Service) -> int:
        """Add a service to the service file and return its new ID."""
        services = self.list_all()
        next_id = max((s.id for s in services), default=0) + 1

        service.id = next_id
        with open(self._file_path, "a") as f:
            f.write(self._to_line(service) + "\n")

        return next_id

    def get_by_id(self, service_id: int) -> Service | None:
        """Read a service by ID from the service file."""
        for service in self.list_all():
            if service.id == service_id:
                return service
        return None

    def list_all(self) -> list[Service]:
        """Read all services from the service file."""
        if not self._file_path.exists():
            return []

        services = []
        with open(self._file_path, "r") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                services.append(self._from_line(line))
        return services

    def update(self, service: Service) -> None:
        """Update an existing service in the service file."""
        services = self.list_all()
        updated = False

        for i, existing in enumerate(services):
            if existing.id == service.id:
                services[i] = service
                updated = True
                break

        if not updated:
            raise ValueError(f"No service found with id {service.id}")

        self._write_all(services)

    def delete(self, service_id: int) -> None:
        """Delete a service by ID from the service file."""
        services = self.list_all()
        remaining = [s for s in services if s.id != service_id]

        if len(remaining) == len(services):
            raise ValueError(f"No service found with id {service_id}")

        self._write_all(remaining)

    # ---------- internal helpers ----------

    def _write_all(self, services: list[Service]) -> None:
        with open(self._file_path, "w") as f:
            for service in services:
                f.write(self._to_line(service) + "\n")

    @staticmethod
    def _to_line(service: Service) -> str:
        return f"{service.id}|{service.name}|{service.price}|{service.duration_minutes}"

    @staticmethod
    def _from_line(line: str) -> Service:
        service_id, name, price, duration_minutes = line.split("|")
        return Service(
            id=int(service_id),
            name=name,
            price=float(price),
            duration_minutes=int(duration_minutes),
        )