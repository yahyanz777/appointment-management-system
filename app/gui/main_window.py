import tkinter as tk
from tkinter import ttk

from app.gui.appointment_panel import AppointmentPanel
from app.gui.customer_panel import CustomerPanel
from app.gui.service_panel import ServicePanel
from app.storage.file_paths import ensure_data_files_exist


class MainWindow:
    """Main tkinter window that routes users to each GUI module."""

    def __init__(self) -> None:
        self.root = tk.Tk()
        self.root.title("Appointment Management System")
        self.root.geometry("720x420")
        self.root.minsize(560, 320)

        self._build_layout()

    def run(self) -> None:
        """Start the GUI application."""
        ensure_data_files_exist()
        self.root.mainloop()

    def _build_layout(self) -> None:
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

        notebook = ttk.Notebook(self.root)
        notebook.grid(row=0, column=0, sticky="nsew")

        notebook.add(CustomerPanel(notebook), text="Customers")
        notebook.add(ServicePanel(notebook), text="Services")
        notebook.add(AppointmentPanel(notebook), text="Appointments")

