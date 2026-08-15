import unittest
from unittest.mock import patch

from app.models.appointment import Appointment
from app.terminal.appointment_menu import AppointmentMenu


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


class AppointmentMenuTest(unittest.TestCase):
    @patch('builtins.input', side_effect=["0"])
    @patch('builtins.print')
    def test_menu_exit(self, mock_print, mock_input) -> None:
        menu = AppointmentMenu()
        menu.run()
        mock_print.assert_any_call("1. Book Appointment")

    @patch('builtins.input', side_effect=["1", "1", "2", "2026-09-01", "10:00", "0"])
    @patch('builtins.print')
    @patch('app.services.appointment_service.AppointmentService.create_appointment', return_value=123)
    def test_menu_book_appointment(self, mock_create, mock_print, mock_input) -> None:
        menu = AppointmentMenu()
        menu.run()
        mock_create.assert_called_once_with(
            customer_id=1,
            service_id=2,
            appointment_date="2026-09-01",
            start_time="10:00"
        )
        mock_print.assert_any_call("Success: Appointment successfully booked (ID: 123).")

    @patch('builtins.input', side_effect=["2", "456", "0"])
    @patch('builtins.print')
    @patch('app.services.appointment_service.AppointmentService.cancel_appointment')
    def test_menu_cancel_appointment(self, mock_cancel, mock_print, mock_input) -> None:
        menu = AppointmentMenu()
        menu.run()
        mock_cancel.assert_called_once_with(456)
        mock_print.assert_any_call("Success: Appointment ID 456 has been cancelled.")


from datetime import datetime, timedelta
from app.services.appointment_service import AppointmentService

class AppointmentServiceValidationTest(unittest.TestCase):
    def setUp(self):
        from unittest.mock import MagicMock
        self.mock_file_handler = MagicMock()
        self.service = AppointmentService(
            self.mock_file_handler,
            customer_exists_checker=lambda x: True,
            service_exists_checker=lambda x: True,
        )

    def test_create_appointment_in_past_raises_value_error(self) -> None:
        past_date = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")
        with self.assertRaises(ValueError) as context:
            self.service.create_appointment(
                customer_id=1,
                service_id=1,
                appointment_date=past_date,
                start_time="10:00"
            )
        self.assertIn("must be in the future", str(context.exception))

    def test_create_appointment_in_future_succeeds(self) -> None:
        future_date = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")
        self.mock_file_handler.list_all.return_value = []
        self.mock_file_handler.add.return_value = 999
        
        appt_id = self.service.create_appointment(
            customer_id=1,
            service_id=1,
            appointment_date=future_date,
            start_time="10:00"
        )
        self.assertEqual(appt_id, 999)


if __name__ == "__main__":
    unittest.main()
