import unittest

from app.gui.appointment_panel import AppointmentPanel
from app.gui.customer_panel import CustomerPanel
from app.gui.main_window import MainWindow
from app.gui.service_panel import ServicePanel


class GuiSkeletonTest(unittest.TestCase):
    def test_gui_classes_can_be_imported(self) -> None:
        self.assertIsNotNone(MainWindow)
        self.assertIsNotNone(CustomerPanel)
        self.assertIsNotNone(ServicePanel)
        self.assertIsNotNone(AppointmentPanel)


if __name__ == "__main__":
    unittest.main()
