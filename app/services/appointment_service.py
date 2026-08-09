from app.models.appointment import Appointment
from app.file_handlers.appointment_file_handler import AppointmentFileHandler


class AppointmentService:
    """Public interface for appointment management use cases."""

    def __init__(self, file_handler: AppointmentFileHandler) -> None:
        self._file_handler = file_handler

    def create_appointment(
        self,
        customer_id: int,
        service_id: int,
        appointment_date: str,
        start_time: str,
    ) -> int:
        """Create an appointment using stable customer and service IDs."""
        # TODO: check customer exists through a stable interface.
        # TODO: check service exists through a stable interface.
        # TODO: check appointment conflicts before saving.
        appointment = Appointment(
            id=None,
            customer_id=customer_id,
            service_id=service_id,
            appointment_date=appointment_date,
            start_time=start_time,
            status="scheduled",
        )
        return self._file_handler.add(appointment)

    def is_time_slot_available(
        self,
        appointment_date: str,
        start_time: str,
        service_id: int,
    ) -> bool:
        """Return whether a time slot is available."""
        raise NotImplementedError("TODO: implement appointment conflict checks")

    def cancel_appointment(self, appointment_id: int) -> None:
        """Cancel an existing appointment."""
        self._file_handler.cancel(appointment_id)
