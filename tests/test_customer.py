import unittest

from app.models.customer import Customer


class CustomerSkeletonTest(unittest.TestCase):
    def test_customer_model_has_expected_fields(self) -> None:
        customer = Customer(
            id=1,
            name="Example Customer",
            phone="555-0100",
            email="customer@example.com",
        )

        self.assertEqual(customer.id, 1)
        self.assertEqual(customer.name, "Example Customer")


if __name__ == "__main__":
    unittest.main()

