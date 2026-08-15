import tkinter as tk
from tkinter import ttk

from app.gui.appointment_panel import AppointmentPanel
from app.gui.customer_panel import CustomerPanel
from app.gui.service_panel import ServicePanel
from app.storage.file_paths import ensure_data_files_exist

class MainWindow:
    def __init__(self):
        # Enable High DPI awareness on Windows for crisp/sharp text
        try:
            import ctypes
            ctypes.windll.shcore.SetProcessDpiAwareness(1)
        except Exception:
            pass

        # Create and setup the main window
        self.root = tk.Tk()
        self.root.title("Appointment Management System")
        self.root.geometry("1280x720")  # Increased size for more content visibility
        self.root.resizable(True, True)   # Allow resizing
        
        # Configure window grid expansion
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        
        # Create tabs container (Notebook)
        notebook = ttk.Notebook(self.root)
        notebook.grid(row=0, column=0, sticky="nsew")
        
        # Add panels to tabs
        notebook.add(CustomerPanel(notebook), text="Customers")
        notebook.add(ServicePanel(notebook), text="Services")
        notebook.add(AppointmentPanel(notebook), text="Appointments")

    def run(self):
        # Ensure data directories/files exist before launching
        ensure_data_files_exist()
        # Start the application loop
        self.root.mainloop()
