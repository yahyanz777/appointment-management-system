from dataclasses import dataclass


@dataclass(slots=True)
class Appointment:
    """Simple appointment data model using IDs from other modules."""

    id: int | None
    customer_id: int
    service_id: int
    appointment_date: str
    start_time: str
    status: str

