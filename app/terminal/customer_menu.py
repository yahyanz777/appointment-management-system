from pathlib import Path

from app.file_handlers.customer_file_handler import CustomerFileHandler
from app.services.customer_service import CustomerService


class CustomerMenu:
    """Terminal menu for customer management."""

    def __init__(self, service: CustomerService | None = None) -> None:
        if service is None:
            file_handler = CustomerFileHandler(Path("data/customers.txt"))
            self._service = CustomerService(file_handler)
        else:
            self._service = service

    def run(self) -> None:
        """Display and handle customer menu choices."""
        while True:
            print("\n=== Customer Management ===")
            print("1. Create Customer")
            print("2. View All Customers")
            print("3. View Customer by ID")
            print("4. Update Customer")
            print("5. Delete Customer")
            print("6. Return to Main Menu")

            choice = input("Enter choice (1-6): ").strip()

            if choice == "1":
                self._create_customer()
            elif choice == "2":
                self._list_customers()
            elif choice == "3":
                self._view_customer()
            elif choice == "4":
                self._update_customer()
            elif choice == "5":
                self._delete_customer()
            elif choice == "6":
                break
            else:
                print("Invalid selection. Please choose a number between 1 and 6.")

    def _create_customer(self) -> None:
        name = input("Enter Name  : ").strip()
        phone = input("Enter Phone : ").strip()
        email = input("Enter Email : ").strip()
        try:
            customer_id = self._service.create_customer(name, phone, email)
            print(f" Success: Created Customer with ID {customer_id}")
        except ValueError as e:
            print(f" Error: {e}")

    def _list_customers(self) -> None:
        customers = self._service.list_customers()
        if not customers:
            print("No customers registered yet.")
        else:
            print("\n--- Customer List ---")
            for c in customers:
                print(f"ID: {c.id} | Name: {c.name} | Phone: {c.phone} | Email: {c.email}")

    def _view_customer(self) -> None:
        raw_id = input("Enter Customer ID: ").strip()
        if not raw_id.isdigit():
            print(" Error: Customer ID must be an integer.")
            return

        c = self._service.get_customer(int(raw_id))
        if c:
            print(f"\nID    : {c.id}\nName  : {c.name}\nPhone : {c.phone}\nEmail : {c.email}")
        else:
            print(" Customer not found.")

    def _update_customer(self) -> None:
        raw_id = input("Enter Customer ID to update: ").strip()
        if not raw_id.isdigit():
            print(" Error: Customer ID must be an integer.")
            return

        cid = int(raw_id)
        c = self._service.get_customer(cid)
        if not c:
            print(" Customer not found.")
            return

        print("(Leave empty to keep existing value)")
        name_input = input(f"New Name [{c.name}]: ").strip()
        phone_input = input(f"New Phone [{c.phone}]: ").strip()
        email_input = input(f"New Email [{c.email}]: ").strip()

        name = name_input if name_input else None
        phone = phone_input if phone_input else None
        email = email_input if email_input else None

        try:
            if self._service.update_customer(cid, name, phone, email):
                print(" Customer updated successfully.")
            else:
                print(" Failed to update customer.")
        except ValueError as e:
            print(f" Error: {e}")

    def _delete_customer(self) -> None:
        raw_id = input("Enter Customer ID to delete: ").strip()
        if not raw_id.isdigit():
            print(" Error: Customer ID must be an integer.")
            return

        cid = int(raw_id)
        if self._service.delete_customer(cid):
            print(" Customer deleted successfully.")
        else:
            print(" Customer not found.")