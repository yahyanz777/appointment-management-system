import csv
from pathlib import Path

from app.models.appointment import Appointment


class AppointmentFileHandler:
    """Handles appointment records stored in a CSV/text file."""

    def __init__(self, file_path: Path) -> None:
        self._file_path = file_path

    def list_all(self) -> list[Appointment]:
        """Read all appointments from the appointment file."""
        if not self._file_path.exists():
            return []

        appointments = []
        with open(self._file_path, mode="r", encoding="utf-8", newline="") as f:
            reader = csv.reader(f)
            for row in reader:
                if not row:
                    continue
                try:
                    appointments.append(
                        Appointment(
                            id=int(row[0]),
                            customer_id=int(row[1]),
                            service_id=int(row[2]),
                            appointment_date=row[3],
                            start_time=row[4],
                            status=row[5],
                        )
                    )
                except (ValueError, IndexError):
                    # Skip malformed lines
                    continue
        return appointments

    def _write_all(self, appointments: list[Appointment]) -> None:
        """Helper to write all appointments to the file."""
        self._file_path.parent.mkdir(parents=True, exist_ok=True)
        with open(self._file_path, mode="w", encoding="utf-8", newline="") as f:
            writer = csv.writer(f)
            for appt in appointments:
                writer.writerow([
                    appt.id,
                    appt.customer_id,
                    appt.service_id,
                    appt.appointment_date,
                    appt.start_time,
                    appt.status,
                ])

    def add(self, appointment: Appointment) -> int:
        """Add an appointment to the appointment file and return its new ID."""
        appointments = self.list_all()
        new_id = len(appointments) + 1
        appointment.id = new_id

        self._file_path.parent.mkdir(parents=True, exist_ok=True)
        with open(self._file_path, mode="a", encoding="utf-8", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([
                appointment.id,
                appointment.customer_id,
                appointment.service_id,
                appointment.appointment_date,
                appointment.start_time,
                appointment.status,
            ])
        return new_id

    def get_by_id(self, appointment_id: int) -> Appointment | None:
        """Read an appointment by ID from the appointment file."""
        if not self._file_path.exists():
            return None

        with open(self._file_path, mode="r", encoding="utf-8", newline="") as f:
            reader = csv.reader(f)
            for row in reader:
                if not row:
                    continue
                try:
                    current_id = int(row[0])
                    if current_id == appointment_id:
                        return Appointment(
                            id=current_id,
                            customer_id=int(row[1]),
                            service_id=int(row[2]),
                            appointment_date=row[3],
                            start_time=row[4],
                            status=row[5],
                        )
                except (ValueError, IndexError):
                    continue
        return None

    def update(self, appointment: Appointment) -> None:
        """Update an existing appointment in the appointment file."""
        if appointment.id is None:
            raise ValueError("Cannot update an appointment without an ID")
        appointments = self.list_all()
        found = False
        for i, appt in enumerate(appointments):
            if appt.id == appointment.id:
                appointments[i] = appointment
                found = True
                break
        if not found:
            raise ValueError(f"Appointment with ID {appointment.id} not found")
        self._write_all(appointments)

    def cancel(self, appointment_id: int) -> None:
        """Mark an appointment as cancelled in the appointment file."""
        appointments = self.list_all()
        found = False
        for appt in appointments:
            if appt.id == appointment_id:
                appt.status = "cancelled"
                found = True
                break
        if not found:
            raise ValueError(f"Appointment with ID {appointment_id} not found")
        self._write_all(appointments)
