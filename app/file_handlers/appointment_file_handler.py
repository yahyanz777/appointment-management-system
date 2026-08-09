from pathlib import Path

from app.models.appointment import Appointment


class AppointmentFileHandler:
    """Handles appointment records stored in a text file."""

    def __init__(self, file_path: Path) -> None:
        self._file_path = file_path

    def add(self, appointment: Appointment) -> int:
        """Add an appointment to the appointment file and return its new ID."""
        raise NotImplementedError("TODO: implement appointment creation")

    def get_by_id(self, appointment_id: int) -> Appointment | None:
        """Read an appointment by ID from the appointment file."""
        raise NotImplementedError("TODO: implement appointment lookup")

    def list_all(self) -> list[Appointment]:
        """Read all appointments from the appointment file."""
        raise NotImplementedError("TODO: implement appointment listing")

    def update(self, appointment: Appointment) -> None:
        """Update an existing appointment in the appointment file."""
        raise NotImplementedError("TODO: implement appointment update")

    def cancel(self, appointment_id: int) -> None:
        """Mark an appointment as cancelled in the appointment file."""
        raise NotImplementedError("TODO: implement appointment cancellation")

