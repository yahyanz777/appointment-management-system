import tkinter as tk
from tkinter import ttk, messagebox
from pathlib import Path

from app.file_handlers.appointment_file_handler import AppointmentFileHandler
from app.services.appointment_service import AppointmentService
from app.storage.file_paths import APPOINTMENTS_FILE

def check_customer_exists(customer_id: int) -> bool:
    try:
        from app.file_handlers.customer_file_handler import CustomerFileHandler
        from app.services.customer_service import CustomerService
        from app.storage.file_paths import CUSTOMERS_FILE

        customer_service = CustomerService(CustomerFileHandler(CUSTOMERS_FILE))
        return customer_service.get_customer(customer_id) is not None
    except (NotImplementedError, ImportError):
        return True

def check_service_exists(service_id: int) -> bool:
    try:
        from app.file_handlers.service_file_handler import ServiceFileHandler
        from app.services.service_service import ServiceService
        from app.storage.file_paths import SERVICES_FILE

        service_service = ServiceService(ServiceFileHandler(SERVICES_FILE))
        return service_service.get_service(service_id) is not None
    except (NotImplementedError, ImportError):
        return True


class AppointmentPanel(ttk.Frame):
    """GUI panel for appointment management."""

    def __init__(self, parent) -> None:
        super().__init__(parent, padding=16)
        self.appointment_service = AppointmentService(
            AppointmentFileHandler(APPOINTMENTS_FILE),
            customer_exists_checker=check_customer_exists,
            service_exists_checker=check_service_exists,
        )
        self._build_layout()
        self._refresh_table()

    def _build_layout(self) -> None:
        # Title Heading
        heading = ttk.Label(
            self, text="Appointment Management", font=("Segoe UI", 14, "bold")
        )
        heading.grid(row=0, column=0, columnspan=2, sticky="w", pady=(0, 12))

        # Input Form Section
        form_frame = ttk.LabelFrame(self, text="Book Appointment", padding=10)
        form_frame.grid(row=1, column=0, columnspan=2, sticky="ew", pady=(0, 12))

        ttk.Label(form_frame, text="Customer ID:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
        self._customer_entry = ttk.Entry(form_frame, width=15)
        self._customer_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(form_frame, text="Service ID:").grid(row=0, column=2, sticky="w", padx=5, pady=5)
        self._service_entry = ttk.Entry(form_frame, width=15)
        self._service_entry.grid(row=0, column=3, padx=5, pady=5)

        ttk.Label(form_frame, text="Date (YYYY-MM-DD):").grid(row=1, column=0, sticky="w", padx=5, pady=5)
        self._date_entry = ttk.Entry(form_frame, width=15)
        self._date_entry.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(form_frame, text="Time (HH:MM):").grid(row=1, column=2, sticky="w", padx=5, pady=5)
        self._time_entry = ttk.Entry(form_frame, width=15)
        self._time_entry.grid(row=1, column=3, padx=5, pady=5)

        # Action Buttons
        btn_frame = ttk.Frame(form_frame)
        btn_frame.grid(row=1, column=4, padx=15, pady=5)

        ttk.Button(btn_frame, text="Book", command=self._book_appointment).pack(side="left", padx=2)
        ttk.Button(btn_frame, text="Clear", command=self._clear_form).pack(side="left", padx=2)

        # Treeview / Table Section
        tree_frame = ttk.Frame(self)
        tree_frame.grid(row=2, column=0, columnspan=2, sticky="nsew")

        self.columnconfigure(0, weight=1)
        self.rowconfigure(2, weight=1)

        self._tree = ttk.Treeview(
            tree_frame,
            columns=("ID", "CustomerID", "ServiceID", "Date", "Time", "Status"),
            show="headings",
            selectmode="browse",
            height=10,
        )
        self._tree.heading("ID", text="ID")
        self._tree.heading("CustomerID", text="Customer ID")
        self._tree.heading("ServiceID", text="Service ID")
        self._tree.heading("Date", text="Date")
        self._tree.heading("Time", text="Time")
        self._tree.heading("Status", text="Status")

        self._tree.column("ID", width=60, anchor="center")
        self._tree.column("CustomerID", width=100, anchor="center")
        self._tree.column("ServiceID", width=100, anchor="center")
        self._tree.column("Date", width=120, anchor="center")
        self._tree.column("Time", width=100, anchor="center")
        self._tree.column("Status", width=120, anchor="center")

        scrollbar = ttk.Scrollbar(
            tree_frame, orient="vertical", command=self._tree.yview
        )
        self._tree.configure(yscroll=scrollbar.set)

        self._tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Action bar at bottom
        actions_frame = ttk.Frame(self)
        actions_frame.grid(row=3, column=0, columnspan=2, sticky="w", pady=(10, 0))

        ttk.Button(actions_frame, text="Cancel Selected", command=self._cancel_appointment).pack(side="left", padx=5)
        ttk.Button(actions_frame, text="Refresh List", command=self._refresh_table).pack(side="left", padx=5)

    def _refresh_table(self) -> None:
        """Reloads appointment records into the Treeview table."""
        for item in self._tree.get_children():
            self._tree.delete(item)

        for appt in self.appointment_service._file_handler.list_all():
            self._tree.insert(
                "",
                "end",
                iid=str(appt.id),
                values=(
                    appt.id,
                    appt.customer_id,
                    appt.service_id,
                    appt.appointment_date,
                    appt.start_time,
                    appt.status,
                ),
            )

    def _book_appointment(self) -> None:
        cust_id_str = self._customer_entry.get().strip()
        svc_id_str = self._service_entry.get().strip()
        date = self._date_entry.get().strip()
        time = self._time_entry.get().strip()

        if not cust_id_str or not svc_id_str or not date or not time:
            messagebox.showwarning("Validation Error", "All fields are required.")
            return

        try:
            cust_id = int(cust_id_str)
            svc_id = int(svc_id_str)
            appt_id = self.appointment_service.create_appointment(
                customer_id=cust_id,
                service_id=svc_id,
                appointment_date=date,
                start_time=time,
            )
            messagebox.showinfo("Success", f"Appointment successfully booked (ID: {appt_id}).")
            self._clear_form()
            self._refresh_table()
        except ValueError as e:
            messagebox.showerror("Error", str(e))
        except Exception as e:
            messagebox.showerror("Unexpected Error", str(e))

    def _cancel_appointment(self) -> None:
        selected_items = self._tree.selection()
        if not selected_items:
            messagebox.showwarning("Selection Required", "Please select an appointment to cancel.")
            return

        appt_id = int(selected_items[0])
        confirm = messagebox.askyesno(
            "Confirm Cancel",
            f"Are you sure you want to cancel appointment ID {appt_id}?",
        )
        if confirm:
            try:
                self.appointment_service.cancel_appointment(appt_id)
                messagebox.showinfo("Success", f"Appointment ID {appt_id} has been cancelled.")
                self._refresh_table()
            except ValueError as e:
                messagebox.showerror("Error", str(e))
            except Exception as e:
                messagebox.showerror("Unexpected Error", str(e))

    def _clear_form(self) -> None:
        self._customer_entry.delete(0, tk.END)
        self._service_entry.delete(0, tk.END)
        self._date_entry.delete(0, tk.END)
        self._time_entry.delete(0, tk.END)
