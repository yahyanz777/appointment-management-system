import argparse

from app.gui.main_window import MainWindow
from app.terminal.main_menu import MainMenu


def main() -> None:
    """Start the appointment management application."""
    parser = argparse.ArgumentParser(description="Appointment Management System")
    parser.add_argument(
        "--gui",
        action="store_true",
        help="start the tkinter GUI instead of the terminal menu",
    )
    args = parser.parse_args()

    if args.gui:
        MainWindow().run()
    else:
        MainMenu().run()


if __name__ == "__main__":
    main()
