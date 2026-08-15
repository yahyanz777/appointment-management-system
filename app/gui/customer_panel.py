from pathlib import Path
import tkinter as tk
from tkinter import messagebox, ttk

from app.file_handlers.customer_file_handler import CustomerFileHandler
from app.services.customer_service import CustomerService


class CustomerPanel(ttk.Frame):
    """GUI panel for patient management."""

    def __init__(
        self, parent: tk.Widget, service: CustomerService | None = None
    ) -> None:
        super().__init__(parent, padding=16)

        if service is None:
            file_handler = CustomerFileHandler(Path("data/customers.txt"))
            self._service = CustomerService(file_handler)
        else:
            self._service = service

        self._selected_customer_id: int | None = None
        self._build_layout()
        self._refresh_customer_list()

    def _build_layout(self) -> None:
        # Title Heading
        heading = ttk.Label(
            self, text="Patient Management", font=("Segoe UI", 14, "bold")
        )
        heading.grid(row=0, column=0, columnspan=2, sticky="w", pady=(0, 12))

        # Input Form Section
        form_frame = ttk.LabelFrame(self, text="Patient Details", padding=10)
        form_frame.grid(row=1, column=0, columnspan=2, sticky="ew", pady=(0, 12))

        ttk.Label(form_frame, text="Name:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
        self._name_entry = ttk.Entry(form_frame, width=25)
        self._name_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(form_frame, text="Phone:").grid(row=0, column=2, sticky="w", padx=5, pady=5)
        self._phone_entry = ttk.Entry(form_frame, width=25)
        self._phone_entry.grid(row=0, column=3, padx=5, pady=5)

        ttk.Label(form_frame, text="Email:").grid(row=1, column=0, sticky="w", padx=5, pady=5)
        self._email_entry = ttk.Entry(form_frame, width=25)
        self._email_entry.grid(row=1, column=1, padx=5, pady=5)

        # Action Buttons
        btn_frame = ttk.Frame(form_frame)
        btn_frame.grid(row=1, column=2, columnspan=2, sticky="e", padx=5, pady=5)

        ttk.Button(btn_frame, text="Add", command=self._add_customer).grid(
            row=0, column=0, padx=2
        )
        ttk.Button(btn_frame, text="Update", command=self._update_customer).grid(
            row=0, column=1, padx=2
        )
        ttk.Button(btn_frame, text="Delete", command=self._delete_customer).grid(
            row=0, column=2, padx=2
        )
        ttk.Button(btn_frame, text="Clear", command=self._clear_form).grid(
            row=0, column=3, padx=2
        )

        # Treeview / Table Section
        tree_frame = ttk.Frame(self)
        tree_frame.grid(row=2, column=0, columnspan=2, sticky="nsew")

        self.columnconfigure(0, weight=1)
        self.rowconfigure(2, weight=1)

        self._tree = ttk.Treeview(
            tree_frame,
            columns=("ID", "Name", "Phone", "Email"),
            show="headings",
            selectmode="browse",
        )
        self._tree.heading("ID", text="ID")
        self._tree.heading("Name", text="Name")
        self._tree.heading("Phone", text="Phone")
        self._tree.heading("Email", text="Email")

        self._tree.column("ID", width=60, anchor="center")
        self._tree.column("Name", width=160, anchor="w")
        self._tree.column("Phone", width=120, anchor="center")
        self._tree.column("Email", width=200, anchor="w")

        scrollbar = ttk.Scrollbar(
            tree_frame, orient="vertical", command=self._tree.yview
        )
        self._tree.configure(yscroll=scrollbar.set)

        self._tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        self._tree.bind("<<TreeviewSelect>>", self._on_select_customer)

    def _refresh_customer_list(self) -> None:
        """Reloads customer records into the Treeview table."""
        for item in self._tree.get_children():
            self._tree.delete(item)

        for customer in self._service.list_customers():
            self._tree.insert(
                "",
                "end",
                values=(customer.id, customer.name, customer.phone, customer.email),
            )

    def _on_select_customer(self, event: tk.Event) -> None:
        """Populates entry fields when a row is clicked in the table."""
        selected_items = self._tree.selection()
        if not selected_items:
            return

        item = self._tree.item(selected_items[0])
        values = item["values"]
        if values:
            self._selected_customer_id = int(values[0])
            self._name_entry.delete(0, tk.END)
            self._name_entry.insert(0, str(values[1]))
            self._phone_entry.delete(0, tk.END)
            self._phone_entry.insert(0, str(values[2]))
            self._email_entry.delete(0, tk.END)
            self._email_entry.insert(0, str(values[3]))

    def _add_customer(self) -> None:
        name = self._name_entry.get().strip()
        phone = self._phone_entry.get().strip()
        email = self._email_entry.get().strip()

        try:
            new_id = self._service.create_customer(name, phone, email)
            messagebox.showinfo("Success", f"Patient registered with ID: {new_id}")
            self._clear_form()
            self._refresh_customer_list()
        except ValueError as e:
            messagebox.showerror("Validation Error", str(e))

    def _update_customer(self) -> None:
        if self._selected_customer_id is None:
            messagebox.showwarning(
                "Selection Required", "Please select a patient from the list to update."
            )
            return

        name = self._name_entry.get().strip()
        phone = self._phone_entry.get().strip()
        email = self._email_entry.get().strip()

        try:
            if self._service.update_customer(
                self._selected_customer_id, name, phone, email
            ):
                messagebox.showinfo("Success", "Patient details updated successfully.")
                self._clear_form()
                self._refresh_customer_list()
            else:
                messagebox.showerror("Error", "Patient not found.")
        except ValueError as e:
            messagebox.showerror("Validation Error", str(e))

    def _delete_customer(self) -> None:
        if self._selected_customer_id is None:
            messagebox.showwarning(
                "Selection Required", "Please select a patient from the list to delete."
            )
            return

        confirm = messagebox.askyesno(
            "Confirm Delete",
            f"Are you sure you want to delete patient ID {self._selected_customer_id}?",
        )
        if confirm:
            if self._service.delete_customer(self._selected_customer_id):
                messagebox.showinfo("Success", "Patient deleted successfully.")
                self._clear_form()
                self._refresh_customer_list()
            else:
                messagebox.showerror("Error", "Failed to delete patient.")

    def _clear_form(self) -> None:
        self._selected_customer_id = None
        self._name_entry.delete(0, tk.END)
        self._phone_entry.delete(0, tk.END)
        self._email_entry.delete(0, tk.END)
        if self._tree.selection():
            self._tree.selection_remove(self._tree.selection())