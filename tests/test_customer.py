from pathlib import Path
import tempfile
import unittest

from app.file_handlers.customer_file_handler import CustomerFileHandler
from app.models.customer import Customer
from app.services.customer_service import CustomerService


class CustomerSkeletonTest(unittest.TestCase):
    """Skeleton test for customer data model."""

    def test_customer_model_has_expected_fields(self) -> None:
        customer = Customer(
            id=1,
            name="Example Customer",
            phone="555-0100",
            email="customer@example.com",
        )

        self.assertEqual(customer.id, 1)
        self.assertEqual(customer.name, "Example Customer")
        self.assertEqual(customer.phone, "555-0100")
        self.assertEqual(customer.email, "customer@example.com")


class CustomerModelTest(unittest.TestCase):
    """Tests for Customer dataclass serialization and formatting."""

    def test_to_and_from_file_line() -> None:
        customer = Customer(
            id=101, name="Ahmed", phone="01012345678", email="ahmed@example.com"
        )
        line = customer.to_file_line()
        self.assertEqual(line, "101|Ahmed|01012345678|ahmed@example.com\n")

        parsed = Customer.from_file_line(line)
        self.assertIsNotNone(parsed)
        if parsed:
            self.assertEqual(parsed.id, 101)
            self.assertEqual(parsed.name, "Ahmed")
            self.assertEqual(parsed.phone, "01012345678")
            self.assertEqual(parsed.email, "ahmed@example.com")

    def test_to_dict() -> None:
        customer = Customer(
            id=102, name="Sara", phone="01122334455", email="sara@example.com"
        )
        data = customer.to_dict()
        self.assertEqual(
            data,
            {
                "id": 102,
                "name": "Sara",
                "phone": "01122334455",
                "email": "sara@example.com",
            },
        )


class CustomerFileHandlerTest(unittest.TestCase):
    """Tests for CustomerFileHandler text storage logic."""

    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.file_path = Path(self.temp_dir.name) / "customers.txt"
        self.file_handler = CustomerFileHandler(self.file_path)

    def tearDown(self) -> None:
        self.temp_dir.cleanup()

    def test_add_auto_increments_id() -> None:
        c1 = Customer(id=None, name="Ali", phone="01000000000", email="ali@example.com")
        c2 = Customer(id=None, name="Omar", phone="01500000000", email="omar@example.com")

        id1 = self.file_handler.add(c1)
        id2 = self.file_handler.add(c2)

        self.assertEqual(id1, 1)
        self.assertEqual(id2, 2)

    def test_get_by_id_and_list_all() -> None:
        c = Customer(id=None, name="Mona", phone="01200000000", email="mona@example.com")
        self.file_handler.add(c)

        retrieved = self.file_handler.get_by_id(1)
        self.assertIsNotNone(retrieved)
        if retrieved:
            self.assertEqual(retrieved.name, "Mona")

        all_customers = self.file_handler.list_all()
        self.assertEqual(len(all_customers), 1)

    def test_update_and_delete() -> None:
        c = Customer(id=None, name="Original", phone="01011111111", email="orig@example.com")
        cid = self.file_handler.add(c)

        updated_customer = Customer(
            id=cid, name="Updated Name", phone="01011111111", email="orig@example.com"
        )
        self.file_handler.update(updated_customer)

        fetched = self.file_handler.get_by_id(cid)
        self.assertIsNotNone(fetched)
        if fetched:
            self.assertEqual(fetched.name, "Updated Name")

        self.file_handler.delete(cid)
        self.assertIsNone(self.file_handler.get_by_id(cid))


class CustomerServiceTest(unittest.TestCase):
    """Tests for CustomerService business logic and validation."""

    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.file_path = Path(self.temp_dir.name) / "customers.txt"
        self.file_handler = CustomerFileHandler(self.file_path)
        self.service = CustomerService(self.file_handler)

    def tearDown(self) -> None:
        self.temp_dir.cleanup()

    def test_create_customer_success() -> None:
        cid = self.service.create_customer("Hassan", "01022223333", "hassan@example.com")
        self.assertEqual(cid, 1)

        customer = self.service.get_customer(cid)
        self.assertIsNotNone(customer)
        if customer:
            self.assertEqual(customer.name, "Hassan")

    def test_validation_empty_name_raises_value_error() -> None:
        with self.assertRaises(ValueError):
            self.service.create_customer("", "01000000000", "test@example.com")

    def test_validation_empty_phone_raises_value_error() -> None:
        with self.assertRaises(ValueError):
            self.service.create_customer("Test User", "   ", "test@example.com")

    def test_validation_invalid_email_raises_value_error() -> None:
        with self.assertRaises(ValueError):
            self.service.create_customer("Test User", "01000000000", "invalid_email")

    def test_update_customer_service() -> None:
        cid = self.service.create_customer("Kareem", "01033334444", "kareem@example.com")
        success = self.service.update_customer(cid, name="Kareem Adel")
        self.assertTrue(success)

        updated = self.service.get_customer(cid)
        self.assertIsNotNone(updated)
        if updated:
            self.assertEqual(updated.name, "Kareem Adel")

    def test_delete_customer_service() -> None:
        cid = self.service.create_customer("Mahmoud", "01044445555", "mahmoud@example.com")
        deleted = self.service.delete_customer(cid)
        self.assertTrue(deleted)
        self.assertIsNone(self.service.get_customer(cid))


if __name__ == "__main__":
    unittest.main()