import tkinter as tk
from tkinter import ttk, messagebox

from app.file_handlers.service_file_handler import ServiceFileHandler
from app.services.service_service import ServiceService
from app.storage.file_paths import SERVICES_FILE


class ServicePanel(ttk.Frame):
    """GUI panel for service management."""

    def __init__(self, parent: tk.Widget) -> None:
        super().__init__(parent, padding=16)
        self._service = ServiceService(ServiceFileHandler(SERVICES_FILE))
        self._build_layout()
        self._refresh_table()

    def _build_layout(self) -> None:
        heading = ttk.Label(self, text="Service Management", font=("Segoe UI", 14, "bold"))
        heading.grid(row=0, column=0, columnspan=4, sticky="w")

        form = ttk.Frame(self)
        form.grid(row=1, column=0, columnspan=4, sticky="w", pady=(12, 8))

        ttk.Label(form, text="Name:").grid(row=0, column=0, sticky="w")
        self._name_entry = ttk.Entry(form)
        self._name_entry.grid(row=0, column=1, padx=5)

        ttk.Label(form, text="Price:").grid(row=0, column=2, sticky="w")
        self._price_entry = ttk.Entry(form, width=10)
        self._price_entry.grid(row=0, column=3, padx=5)

        ttk.Label(form, text="Duration (min):").grid(row=0, column=4, sticky="w")
        self._duration_entry = ttk.Entry(form, width=10)
        self._duration_entry.grid(row=0, column=5, padx=5)

        ttk.Button(form, text="Add Service", command=self._on_add).grid(row=0, column=6, padx=10)

        columns = ("id", "name", "price", "duration")
        self._table = ttk.Treeview(self, columns=columns, show="headings", height=8)
        for col in columns:
            self._table.heading(col, text=col.capitalize())
        self._table.grid(row=2, column=0, columnspan=4, sticky="nsew")

        buttons = ttk.Frame(self)
        buttons.grid(row=3, column=0, columnspan=4, sticky="w", pady=(8, 0))
        ttk.Button(buttons, text="Delete Selected", command=self._on_delete).pack(side="left")
        ttk.Button(buttons, text="Refresh", command=self._refresh_table).pack(side="left", padx=5)

    def _refresh_table(self) -> None:
        for row in self._table.get_children():
            self._table.delete(row)
        for service in self._service.list_services():
            self._table.insert(
                "",
                "end",
                iid=str(service.id),
                values=(service.id, service.name, service.price, service.duration_minutes),
            )

    def _on_add(self) -> None:
        name = self._name_entry.get().strip()
        price = self._price_entry.get().strip()
        duration = self._duration_entry.get().strip()

        try:
            self._service.create_service(name, price, duration)
            self._name_entry.delete(0, tk.END)
            self._price_entry.delete(0, tk.END)
            self._duration_entry.delete(0, tk.END)
            self._refresh_table()
        except ValueError as e:
            messagebox.showerror("Invalid service", str(e))

    def _on_delete(self) -> None:
        selected = self._table.selection()
        if not selected:
            messagebox.showinfo("No selection", "Select a service to delete first.")
            return

        service_id = int(selected[0])
        try:
            self._service.delete_service(service_id)
            self._refresh_table()
        except ValueError as e:
            messagebox.showerror("Not found", str(e))