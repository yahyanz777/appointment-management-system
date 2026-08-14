import tkinter as tk
from tkinter import ttk

class CustomerPanel(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent, padding=16)
        
        # Title of the panel
        heading = ttk.Label(self, text="Customer Management", font=("Arial", 14, "bold"))
        heading.grid(row=0, column=0, sticky="w")
        
        # Message placeholder
        message = ttk.Label(self, text="TODO: Add customer forms, actions, and lists here.")
        message.grid(row=1, column=0, sticky="w", pady=10)
