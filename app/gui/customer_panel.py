import tkinter as tk
from tkinter import ttk


class CustomerPanel(ttk.Frame):
    """Placeholder GUI panel for customer management."""

    def __init__(self, parent: tk.Widget) -> None:
        super().__init__(parent, padding=16)
        self._build_layout()

    def _build_layout(self) -> None:
        heading = ttk.Label(self, text="Customer Management", font=("Segoe UI", 14, "bold"))
        heading.grid(row=0, column=0, sticky="w")

        message = ttk.Label(
            self,
            text="TODO: add customer forms, actions, and list views here.",
            wraplength=520,
        )
        message.grid(row=1, column=0, sticky="w", pady=(8, 0))

