import tempfile
import unittest
from pathlib import Path

from app.models.service import Service
from app.file_handlers.service_file_handler import ServiceFileHandler
from app.services.service_service import ServiceService


class ServiceSkeletonTest(unittest.TestCase):
    def test_service_model_has_expected_fields(self) -> None:
        service = Service(
            id=1,
            name="Consultation",
            price=50.0,
            duration_minutes=30,
        )

        self.assertEqual(service.price, 50.0)
        self.assertEqual(service.duration_minutes, 30)


class ServiceFileHandlerTest(unittest.TestCase):
    def setUp(self) -> None:
        self._tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".txt")
        self._tmp.close()
        self.handler = ServiceFileHandler(Path(self._tmp.name))

    def tearDown(self) -> None:
        Path(self._tmp.name).unlink(missing_ok=True)

    def test_add_assigns_incrementing_ids(self) -> None:
        first_id = self.handler.add(Service(id=None, name="Haircut", price=25.0, duration_minutes=30))
        second_id = self.handler.add(Service(id=None, name="Massage", price=60.0, duration_minutes=45))
        self.assertEqual(first_id, 1)
        self.assertEqual(second_id, 2)

    def test_get_by_id(self) -> None:
        new_id = self.handler.add(Service(id=None, name="Haircut", price=25.0, duration_minutes=30))
        found = self.handler.get_by_id(new_id)
        self.assertIsNotNone(found)
        self.assertEqual(found.name, "Haircut")

    def test_get_by_id_missing_returns_none(self) -> None:
        self.assertIsNone(self.handler.get_by_id(999))

    def test_update(self) -> None:
        new_id = self.handler.add(Service(id=None, name="Haircut", price=25.0, duration_minutes=30))
        updated = Service(id=new_id, name="Haircut", price=30.0, duration_minutes=30)
        self.handler.update(updated)
        self.assertEqual(self.handler.get_by_id(new_id).price, 30.0)

    def test_delete(self) -> None:
        new_id = self.handler.add(Service(id=None, name="Haircut", price=25.0, duration_minutes=30))
        self.handler.delete(new_id)
        self.assertIsNone(self.handler.get_by_id(new_id))


class ServiceServiceTest(unittest.TestCase):
    def setUp(self) -> None:
        self._tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".txt")
        self._tmp.close()
        self.service = ServiceService(ServiceFileHandler(Path(self._tmp.name)))

    def tearDown(self) -> None:
        Path(self._tmp.name).unlink(missing_ok=True)

    def test_create_service(self) -> None:
        new_id = self.service.create_service("Haircut", 25, 30)
        found = self.service.get_service(new_id)
        self.assertEqual(found.name, "Haircut")

    def test_create_service_rejects_negative_price(self) -> None:
        with self.assertRaises(ValueError):
            self.service.create_service("Haircut", -5, 30)

    def test_create_service_rejects_zero_duration(self) -> None:
        with self.assertRaises(ValueError):
            self.service.create_service("Haircut", 25, 0)

    def test_update_service(self) -> None:
        new_id = self.service.create_service("Massage", 60, 45)
        self.service.update_service(new_id, price=75)
        self.assertEqual(self.service.get_service(new_id).price, 75)

    def test_delete_service(self) -> None:
        new_id = self.service.create_service("Massage", 60, 45)
        self.service.delete_service(new_id)
        self.assertIsNone(self.service.get_service(new_id))


if __name__ == "__main__":
    unittest.main()