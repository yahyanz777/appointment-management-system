from app.file_handlers.appointment_file_handler import AppointmentFileHandler
from app.services.appointment_service import AppointmentService
from app.storage.file_paths import APPOINTMENTS_FILE

from app.file_handlers.customer_file_handler import CustomerFileHandler
from app.services.customer_service import CustomerService
from app.storage.file_paths import CUSTOMERS_FILE

from app.file_handlers.service_file_handler import ServiceFileHandler
from app.services.service_service import ServiceService
from app.storage.file_paths import SERVICES_FILE


def check_customer_exists(customer_id: int) -> bool:
    try:
        from app.file_handlers.customer_file_handler import CustomerFileHandler
        from app.services.customer_service import CustomerService
        from app.storage.file_paths import CUSTOMERS_FILE

        customer_service = CustomerService(CustomerFileHandler(CUSTOMERS_FILE))
        return customer_service.get_customer(customer_id) is not None
    except NotImplementedError:
        # Fallback if Customer service/file handler is not implemented
        return True


def check_service_exists(service_id: int) -> bool:
    try:
        from app.file_handlers.service_file_handler import ServiceFileHandler
        from app.services.service_service import ServiceService
        from app.storage.file_paths import SERVICES_FILE

        service_service = ServiceService(ServiceFileHandler(SERVICES_FILE))
        return service_service.get_service(service_id) is not None
    except NotImplementedError:
        # Fallback if Service service/file handler is not implemented
        return True


class AppointmentMenu:
    """Terminal menu for appointment management."""

    def __init__(self) -> None:
        self.appointment_service = AppointmentService(
            AppointmentFileHandler(APPOINTMENTS_FILE),
            customer_exists_checker=check_customer_exists,
            service_exists_checker=check_service_exists,
        )

    def run(self) -> None:
        """Display the appointment menu and handle user choice."""
        while True:
            print("\nAppointment Management")
            print("1. Book Appointment")
            print("2. Cancel Appointment")
            print("3. List All Appointments")
            print("0. Back to Main Menu")

            choice = input("Choose an option: ").strip()

            if choice == "1":
                self._book_appointment()
            elif choice == "2":
                self._cancel_appointment()
            elif choice == "3":
                self._list_appointments()
            elif choice == "0":
                break
            else:
                print("Invalid option. Please try again.")

    def _book_appointment(self) -> None:
        print("\n--- Book Appointment ---")
        try:
            customer_id_str = input("Enter Patient ID: ").strip()
            service_id_str = input("Enter Service ID: ").strip()
            date = input("Enter Date (YYYY-MM-DD): ").strip()
            time = input("Enter Start Time (HH:MM): ").strip()

            if not customer_id_str or not service_id_str:
                print("Error: Patient ID and Service ID cannot be empty.")
                return

            customer_id = int(customer_id_str)
            service_id = int(service_id_str)

            appt_id = self.appointment_service.create_appointment(
                customer_id=customer_id,
                service_id=service_id,
                appointment_date=date,
                start_time=time,
            )
            print(f"Success: Appointment successfully booked (ID: {appt_id}).")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

    def _cancel_appointment(self) -> None:
        print("\n--- Cancel Appointment ---")
        try:
            appt_id_str = input("Enter Appointment ID: ").strip()
            if not appt_id_str:
                print("Error: Appointment ID cannot be empty.")
                return

            appt_id = int(appt_id_str)
            self.appointment_service.cancel_appointment(appt_id)
            print(f"Success: Appointment ID {appt_id} has been cancelled.")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

    def _list_appointments(self) -> None:
        print("\n--- List Appointments ---")
        try:
            appointments = self.appointment_service._file_handler.list_all()
            if not appointments:
                print("No appointments found.")
                return

            try:
                customer_service = CustomerService(CustomerFileHandler(CUSTOMERS_FILE))
                patients = {p.id: p.name for p in customer_service.list_customers()}
            except Exception:
                patients = {}

            try:
                service_service = ServiceService(ServiceFileHandler(SERVICES_FILE))
                services = {s.id: s.name for s in service_service.list_services()}
            except Exception:
                services = {}

            print(
                f"{'ID':<5} | {'Patient':<20} | {'Service':<20} | {'Date':<10} | {'Time':<5} | {'Status':<10}"
            )
            print("-" * 79)
            for appt in appointments:
                patient_name = patients.get(appt.customer_id, f"Patient {appt.customer_id}")
                service_name = services.get(appt.service_id, f"Service {appt.service_id}")
                if len(patient_name) > 20:
                    patient_name = patient_name[:17] + "..."
                if len(service_name) > 20:
                    service_name = service_name[:17] + "..."
                print(
                    f"{appt.id:<5} | {patient_name:<20} | {service_name:<20} | {appt.appointment_date:<10} | {appt.start_time:<5} | {appt.status:<10}"
                )
        except Exception as e:
            print(f"Error listing appointments: {e}")
