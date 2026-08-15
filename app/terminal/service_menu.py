from app.file_handlers.service_file_handler import ServiceFileHandler
from app.services.service_service import ServiceService
from app.storage.file_paths import SERVICES_FILE


class ServiceMenu:
    """Terminal menu for service management."""

    def __init__(self) -> None:
        self._service = ServiceService(ServiceFileHandler(SERVICES_FILE))

    def run(self) -> None:
        """Display the service menu until the user chooses to go back."""
        while True:
            print("\nService Management")
            print("1. Add service")
            print("2. View all services")
            print("3. Update service")
            print("4. Delete service")
            print("0. Back to main menu")

            choice = input("Choose an option: ").strip()

            if choice == "1":
                self._add_service()
            elif choice == "2":
                self._view_services()
            elif choice == "3":
                self._update_service()
            elif choice == "4":
                self._delete_service()
            elif choice == "0":
                break
            else:
                print("Invalid option. Please try again.")

    def _add_service(self) -> None:
        name = input("Service name: ").strip()
        price = input("Price: ").strip()
        duration = input("Duration (minutes): ").strip()

        try:
            new_id = self._service.create_service(name, price, duration)
            print(f"Created service #{new_id}.")
        except ValueError as e:
            print(f"Could not create service: {e}")

    def _view_services(self) -> None:
        services = self._service.list_services()
        if not services:
            print("No services yet.")
            return

        for s in services:
            print(f"[{s.id}] {s.name} - ${s.price:.2f} - {s.duration_minutes} min")

    def _update_service(self) -> None:
        raw_id = input("Service id to update: ").strip()
        try:
            service_id = int(raw_id)
        except ValueError:
            print("Service id must be a number.")
            return

        name = input("New name (leave blank to keep current): ").strip()
        price = input("New price (leave blank to keep current): ").strip()
        duration = input("New duration in minutes (leave blank to keep current): ").strip()

        try:
            self._service.update_service(
                service_id,
                name=name or None,
                price=float(price) if price else None,
                duration_minutes=int(duration) if duration else None,
            )
            print("Service updated.")
        except ValueError as e:
            print(f"Could not update service: {e}")

    def _delete_service(self) -> None:
        raw_id = input("Service id to delete: ").strip()
        try:
            service_id = int(raw_id)
        except ValueError:
            print("Service id must be a number.")
            return

        try:
            self._service.delete_service(service_id)
            print("Service deleted.")
        except ValueError as e:
            print(f"Could not delete service: {e}")