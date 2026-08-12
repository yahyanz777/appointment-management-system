import tkinter as tk
from tkinter import ttk


class ServicePanel(ttk.Frame):
    """Placeholder GUI panel for service management."""

    def __init__(self, parent: tk.Widget) -> None:
        super().__init__(parent, padding=16)
        self._build_layout()

    def _build_layout(self) -> None:
        heading = ttk.Label(self, text="Service Management", font=("Segoe UI", 14, "bold"))
        heading.grid(row=0, column=0, sticky="w")

        message = ttk.Label(
            self,
            text="TODO: add service forms, pricing fields, and duration controls here.",
            wraplength=520,
        )
        message.grid(row=1, column=0, sticky="w", pady=(8, 0))

