from pathlib import Path


BASE_DIR = Path(__file__).resolve().parents[2]
DATA_DIR = BASE_DIR / "data"

CUSTOMERS_FILE = DATA_DIR / "customers.txt"
SERVICES_FILE = DATA_DIR / "services.txt"
APPOINTMENTS_FILE = DATA_DIR / "appointments.txt"


def ensure_data_files_exist() -> None:
    """Create the data folder and empty text files if they do not exist."""
    DATA_DIR.mkdir(exist_ok=True)

    for file_path in (CUSTOMERS_FILE, SERVICES_FILE, APPOINTMENTS_FILE):
        file_path.touch(exist_ok=True)

