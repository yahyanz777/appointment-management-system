# Appointment Management System

A beginner-friendly Python project skeleton for a 3-person team. The application will eventually manage customers, services, and appointments while preventing scheduling conflicts.

This project currently contains the foundation only. Business features are marked with TODO comments and should be implemented by the assigned module owner.

## Technologies

- Python 3
- Text-file handling
- Terminal menus
- Standard Python libraries

No database, GUI framework, Flask, Django, networking, APIs, data science, reports, analytics, or search functionality are included.

## Architecture

The project is split into three independent feature modules:

- Customer Management
- Service Management
- Appointment Management

Each module owns its model, file handler, service, terminal menu, and tests. Modules should communicate through stable IDs and public service methods, not by importing each other's internal implementation details.

```text
main.py
app/
  models/
  file_handlers/
  services/
  storage/
  terminal/
tests/
```

## Team Responsibilities

### Developer 1: Customer Management

Main files:

- `app/models/customer.py`
- `app/file_handlers/customer_file_handler.py`
- `app/services/customer_service.py`
- `app/terminal/customer_menu.py`
- `tests/test_customer.py`

Responsibilities:

- Creating customers
- Updating customers
- Deleting customers
- Viewing customer information
- Customer validation

### Developer 2: Service Management

Main files:

- `app/models/service.py`
- `app/file_handlers/service_file_handler.py`
- `app/services/service_service.py`
- `app/terminal/service_menu.py`
- `tests/test_service.py`

Responsibilities:

- Creating services
- Updating services
- Deleting services
- Viewing services
- Managing service price and duration

### Developer 3: Appointment Management

Main files:

- `app/models/appointment.py`
- `app/file_handlers/appointment_file_handler.py`
- `app/services/appointment_service.py`
- `app/terminal/appointment_menu.py`
- `tests/test_appointment.py`

Responsibilities:

- Creating appointments
- Cancelling appointments
- Rescheduling appointments
- Checking appointment conflicts
- Checking whether a time slot is available

## Shared Files

These files should be changed carefully because all developers depend on them:

- `main.py`
- `app/storage/file_paths.py`
- `app/terminal/main_menu.py`
- `README.md`
- Shared configuration files such as `.gitignore` and `requirements.txt`

Discuss shared-file changes before opening a pull request.

## Install and Run

Create and activate a virtual environment:

```bash
python -m venv .venv
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python main.py
```

The app will create simple text files inside the local `data/` folder.

## Run Tests

```bash
python -m unittest discover
```

## Git Workflow

Use `main` as the stable branch. Each developer works on a feature branch and opens a pull request into `main`.

Suggested branches:

- `developer-1-customer`
- `developer-2-service`
- `developer-3-appointment`

Example:

```bash
git checkout main
git pull origin main
git checkout -b developer-1-customer
git add .
git commit -m "Add customer management skeleton work"
git push -u origin developer-1-customer
```

Before opening a pull request:

```bash
git checkout main
git pull origin main
git checkout developer-1-customer
git merge main
python -m unittest discover
```

## Module Communication Rules

- Use IDs such as `customer_id` and `service_id` between modules.
- Do not import another developer's file handler implementation directly.
- Keep cross-module behavior in service-layer public methods.
- Coordinate before changing shared file paths or the main terminal menu.

For example, appointment code may store `customer_id` and `service_id`, but it should not depend on how customers or services are created internally.

## File Storage Plan

The project uses simple text files for beginner-friendly file handling:

- `data/customers.txt`
- `data/services.txt`
- `data/appointments.txt`

These files are created automatically when the program starts and are ignored by Git.
