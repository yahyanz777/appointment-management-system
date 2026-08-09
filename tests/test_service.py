import unittest

from app.models.service import Service


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


if __name__ == "__main__":
    unittest.main()

