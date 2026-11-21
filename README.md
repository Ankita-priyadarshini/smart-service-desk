
# Smart Service Desk Management System

A Python-based command-line application for managing IT service requests raised by employees. The system allows users to create, view, search and resolve service requests, with persistent JSON storage and structured exception handling.

## Features

- **Create Service Requests:** Register IT support requests with an employee name, issue description and priority.
- **View All Requests:** Display all previously created service requests.
- **Search Requests:** Retrieve a specific request using its unique request ID.
- **Resolve Requests:** Update the status of an open request to resolved.
- **Request ID Validation:** Enforce a consistent `SR` followed by exactly three digits format (e.g., `SR101`). Lowercase input is normalized to uppercase.
- **Priority Validation:** Accept only LOW, MEDIUM and HIGH priorities.
- **Duplicate Prevention:** Prevent multiple requests from being registered with the same ID.
- **JSON Persistence:** Store requests in a JSON file so data remains available between application runs.
- **Custom Exception Handling:** Handle application-specific errors with meaningful messages.

## Technology Stack

- **Language:** Python 3
- **Storage:** JSON
- **Version Control:** Git and GitHub
- **Concepts:** Object-Oriented Programming (OOP), SOLID principles, layered architecture and basic Domain-Driven Design (DDD).

## Project Structure

```text
smart-service-desk/
│
├── domain/
│   ├── __init__.py
│   ├── exceptions.py
│   └── service_request.py
│
├── application/
│   ├── __init__.py
│   └── request_service.py
│
├── infrastructure/
│   ├── __init__.py
│   └── file_repository.py
│
├── data/
│   └── requests.json
│
├── main.py
├── README.md
└── .gitignore
```

## Architecture and Responsibilities

The application follows a layered architecture to separate business logic, application operations and data storage.

### 1. Domain Layer (`domain/`)

Contains the core business entities and rules.

- `service_request.py`: Defines the `ServiceRequest` class, its attributes, validation rules, status management and serialization methods.
- `exceptions.py`: Defines custom exceptions for invalid request IDs, duplicate requests, missing requests, invalid priorities and other application errors.

### 2. Application Layer (`application/`)

Contains the application-level operations.

- `request_service.py`: Handles request creation, retrieval, searching, duplicate checking and resolution.

### 3. Infrastructure Layer (`infrastructure/`)

Handles data persistence.

- `file_repository.py`: Implements JSON-based storage by loading and saving service requests.

### 4. Presentation Layer (`main.py`)

Provides an interactive command-line interface through which users interact with the application.

## Prerequisites

- Python 3.10 or later
- Git

No external Python packages are required.

## Setup and Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Ankita-priyadarshini/smart-service-desk.git
cd smart-service-desk
```

### 2. Create a Virtual Environment

```bash
python3 -m venv venv
```

### 3. Activate the Virtual Environment

**On Linux/macOS:**

```bash
source venv/bin/activate
```

**On Windows:**

```bash
venv\Scripts\activate
```

### 4. Run the Application

```bash
python main.py
```

## Application Menu

The application provides the following operations:

```text
===== SMART SERVICE DESK =====

1. Create Service Request
2. View All Requests
3. Search Request
4. Resolve Request
5. Exit
```

Select an option and follow the prompts displayed in the terminal.

## Request Data Format

Each service request is stored as a JSON object.

Example:

```json
{
    "request_id": "SR101",
    "employee_name": "Rahul",
    "issue": "Laptop is not starting",
    "priority": "HIGH",
    "status": "OPEN"
}
```

### Validation Rules

| Field | Validation |
|---|---|
| Request ID | Must follow `SR` + 3 digits |
| Employee Name | Cannot be empty |
| Issue Description | Cannot be empty |
| Priority | LOW, MEDIUM or HIGH |
| Status | OPEN or RESOLVED |

## Design Principles

The project incorporates the following software engineering principles:

- **Encapsulation:** The service request manages its internal status through methods.
- **Single Responsibility Principle:** Domain logic, application operations and persistence are separated into distinct modules.
- **Dependency Inversion Principle:** The application service receives its repository as a dependency.
- **Separation of Concerns:** Each layer has a clearly defined responsibility.
- **Custom Exception Handling:** Application-specific exceptions provide meaningful error messages.

## Data Persistence

Service requests are stored in `data/requests.json`.

- Existing requests are loaded when the application starts.
- New requests are saved after creation.
- Updated request statuses are saved after resolution.
- Data remains available across application restarts.

## Version Control

The project uses Git for version control and follows a branch-based development workflow.

- `main`: Stable project branch.
- `development`: Branch used for ongoing implementation and testing.

Changes are committed in meaningful stages and merged into `main` after verification.

## Future Enhancements

Potential extensions include:

- Automatic request ID generation.
- Request creation and resolution timestamps.
- Updating request priority.
- Unit testing with Python's `unittest` framework.
