# Job Application Tracker

A Python application for managing job applications.

## Features

- Add job applications
- List all applications
- Search applications by company or position
- Update application status
- Delete applications
- Persistent JSON storage
- Input validation and error handling
- Automated tests with pytest

## Application Statuses

Applications can have one of the following statuses:

- Applied
- OA
- Interview
- Rejected
- Offer
- Withdrawn

## Project Structure

```text
job-application-tracker/
├── application.py       # Application model
├── tracker.py           # Application management logic
├── storage.py           # JSON persistence
├── main.py              # Command-line interface
├── tests/
│   ├── test_application.py
│   ├── test_tracker.py
│   └── test_storage.py
├── requirements.txt
└── README.md
```

## Installation

Clone the repository and navigate to the project directory

```bash
git clone https://github.com/Aleps-ops/job-application-tracker.git
cd job-application-tracker
```

Create a virtual environment

## Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

## Usage
Run the application with:

```bash
python main.py
```

The application provides the following options:

```text
1. List applications
2. Add application
3. Search applications
4. Update status
5. Delete application
6. Exit
```

Application data is automatically stored in applications.json so that applications persist between sessions.

## Running Tests

Run the automated test suite with:

```bash
python -m pytest
```

The project currently includes tests covering the application model, tracker functionality, and JSON storage.

## Technologies

- Python 3
- pytest
- JSON
- Git