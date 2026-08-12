from datetime import datetime

from app.models.appointment import Appointment
from app.file_handlers.appointment_file_handler import AppointmentFileHandler


class AppointmentService:

    def __init__(
        self,
        file_handler: AppointmentFileHandler,
        customer_exists_checker=None,
        service_exists_checker=None,
    ):
        self._file_handler = file_handler
        self._customer_exists_checker = customer_exists_checker
        self._service_exists_checker = service_exists_checker

    def create_appointment(
        self,
        customer_id: int,
        service_id: int,
        appointment_date: str,
        start_time: str,
    ) -> int:

        self._validate_appointment_input(
            customer_id,
            service_id,
            appointment_date,
            start_time,
        )

        if self._customer_exists_checker is not None:
            if not self._customer_exists_checker(customer_id):
                raise ValueError(
                    f"Customer {customer_id} does not exist"
                )

        if self._service_exists_checker is not None:
            if not self._service_exists_checker(service_id):
                raise ValueError(
                    f"Service {service_id} does not exist"
                )
            
        if not self.is_time_slot_available(
            appointment_date,
            start_time,
            service_id,
        ):
            raise ValueError("Selected time slot is not available")

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

        if not isinstance(service_id, int) or service_id <= 0:
            raise ValueError("service_id must be a positive integer")

        appointments = self._file_handler.list_all()

        for appointment in appointments:

            if appointment.status.lower() == "cancelled":
                continue

            if (
                appointment.appointment_date == appointment_date
                and appointment.start_time == start_time
                and appointment.service_id == service_id
            ):
                return False

        return True

    def cancel_appointment(self, appointment_id: int) -> None:
        self._file_handler.cancel(appointment_id)

    def _validate_appointment_input(
        self,
        customer_id: int,
        service_id: int,
        appointment_date: str,
        start_time: str,
    ) -> None:

        if not isinstance(customer_id, int) or customer_id <= 0:
            raise ValueError("customer_id must be a positive integer")

        if not isinstance(service_id, int) or service_id <= 0:
            raise ValueError("service_id must be a positive integer")

        if not self._is_valid_date(appointment_date):
            raise ValueError(
                "appointment_date must be in YYYY-MM-DD format"
            )

        if not self._is_valid_time(start_time):
            raise ValueError(
                "start_time must be in HH:MM format"
            )

    @staticmethod
    def _is_valid_date(value: str) -> bool:
        try:
            datetime.strptime(value, "%Y-%m-%d")
            return True
        except (TypeError, ValueError):
            return False

    @staticmethod
    def _is_valid_time(value: str) -> bool:
        try:
            datetime.strptime(value, "%H:%M")
            return True
        except (TypeError, ValueError):
            return False