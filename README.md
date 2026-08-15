# Hospital Appointment Management System

A robust, lightweight Python application designed to streamline appointment scheduling, patient record management, and healthcare service coordination. The system is equipped with both a sleek graphical user interface (GUI) built with Tkinter and an intuitive Terminal-based command-line interface.

It features comprehensive validation rules, conflict detection, and seamless mapping of patients and services.

---

## Key Features

* **Patient Management**:
  * Register, update, delete, and view patients.
  * Ensures formatting validation for key patient fields (name, phone, and email).
* **Service Management**:
  * Manage clinical and hospital services (e.g., General Consultation, Dentistry, cardiology).
  * Configure service details including consultation fees and session durations.
* **Appointment Booking**:
  * Book and cancel medical appointments.
  * Automatically resolves patient and service IDs into corresponding names in listings for enhanced readability.
  * **Conflict Prevention**: Ensures time slots are not double-booked for the same service.
  * **Future-Date Validation**: Prevents booking appointments in the past relative to the current local system datetime.

---

## Architecture

The system utilizes a modular layer-based architecture implementing a clean separation of concerns:

```text
main.py                   # Application Entrypoint
app/
  models/                 # Data representations (Patient, Service, Appointment)
  file_handlers/          # Data persistence layer (CRUD operations on local text files)
  services/               # Business logic and validation layer
  storage/                # Storage paths and environment setup
  terminal/               # Console-based interactive user interface
  gui/                    # Tkinter-based graphical user interface
tests/                    # Automated testing suite
```

---

## Installation & Run

### 1. Prerequisites
Ensure you have **Python 3.10+** installed on your system.

### 2. Setup Virtual Environment

Create and activate a virtual environment:

```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# macOS / Linux
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Run the Application

The application can be executed in either of two modes:

* **Graphical User Interface (GUI) Mode**:
  ```bash
  python main.py --gui
  ```

* **Interactive Terminal Mode**:
  ```bash
  python main.py
  ```

*Upon execution, the system initializes data persistence files automatically under the local `/data` directory.*

---

## Running the Tests

To run the automated unittest suite and verify validation logic:

```bash
python -m unittest discover -s tests
```

---

## Persistent Storage Plan

The persistence layer stores structured data in plain text/CSV files inside the local `/data` directory:

* `data/customers.txt`: Pipelines-delimited records of patients (`id|name|phone|email`).
* `data/services.txt`: Pipelines-delimited records of medical services (`id|name|fee|duration`).
* `data/appointments.txt`: CSV-formatted records of appointments (`id,patient_id,service_id,date,time,status`).
