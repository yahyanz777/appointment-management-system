import unittest

from app.models.appointment import Appointment


class AppointmentSkeletonTest(unittest.TestCase):
    def test_appointment_model_uses_customer_and_service_ids(self) -> None:
        appointment = Appointment(
            id=1,
            customer_id=10,
            service_id=20,
            appointment_date="2026-08-10",
            start_time="09:00",
            status="scheduled",
        )

        self.assertEqual(appointment.customer_id, 10)
        self.assertEqual(appointment.service_id, 20)


if __name__ == "__main__":
    unittest.main()

