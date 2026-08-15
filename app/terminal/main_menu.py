from app.storage.file_paths import ensure_data_files_exist
from app.terminal.appointment_menu import AppointmentMenu
from app.terminal.customer_menu import CustomerMenu
from app.terminal.service_menu import ServiceMenu


class MainMenu:
    """Simple terminal menu that routes users to each module."""

    def run(self) -> None:
        """Show the main menu until the user chooses to exit."""
        ensure_data_files_exist()

        while True:
            print("\nHospital Appointment Management System")
            print("1. Patient Management")
            print("2. Service Management")
            print("3. Appointment Management")
            print("0. Exit")

            choice = input("Choose an option: ").strip()

            if choice == "1":
                CustomerMenu().run()
            elif choice == "2":
                ServiceMenu().run()
            elif choice == "3":
                AppointmentMenu().run()
            elif choice == "0":
                print("Goodbye.")
                break
            else:
                print("Invalid option. Please try again.")

