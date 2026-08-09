from app.terminal.main_menu import MainMenu


def main() -> None:
    """Start the terminal application."""
    menu = MainMenu()
    menu.run()


if __name__ == "__main__":
    main()
