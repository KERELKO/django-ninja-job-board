# Job Board Project

This project is a web application built using Django framework, django-ninja, Docker, and PostgreSQL. It provides common job board features such as filtering vacancies and filtering candidates who have applied for a vacancy to find the best match.

## Technologies Used

- Django: A high-level Python web framework that encourages rapid development and clean, pragmatic design.
- django-ninja: A powerful library for building APIs in Django with flexible and fast development.
- Docker: A platform for developing, shipping, and running applications in containers.
- PostgreSQL: An open-source relational database management system known for its reliability and robustness.
- Makefile: A simple way to organize code compilation, executable file management, and other tasks.

## Installation

To run this project locally, follow these steps:

1. Clone this repository.
2. Install Docker on your machine if you haven't already.
3. Run `make build` to build the Docker image.
4. Run `make start` to start the Docker container.
5. Access the application at `http://localhost:8000`.

## Usage

Once the application is running, you can access the job board features through the web interface. Users can filter vacancies based on various criteria and also filter candidates who have applied for a vacancy to find the best match.

## Contributing

If you'd like to contribute to this project, feel free to fork the repository and submit a pull request. Please follow the existing code style and ensure that all tests pass before submitting your changes.

## Project structure
```
├── docker-compose.yaml
├── Dockerfile
├── Makefile
├── manage.py
├── poetry.lock
├── pyproject.toml
├── README.md
├── src
│   ├── api
│   │   ├── __init__.py
│   │   ├── schemas.py
│   │   ├── urls.py
│   │   └── v1
│   │       ├── __init__.py
│   │       ├── profiles
│   │       │   ├── employers
│   │       │   ├── __init__.py
│   │       │   └── jobseekers
│   │       ├── users
│   │       └── vacancies
│   │           ├── handlers.py
│   │           ├── __init__.py
│   │           └── schemas.py
│   ├── apps
│   │   ├── __init__.py
│   │   ├── profiles
│   │   │   ├── admin.py
│   │   │   ├── apps.py
│   │   │   ├── converters
│   │   │   │   ├── __init__.py
│   │   │   │   └── profiles
│   │   │   ├── entities
│   │   │   │   └── profiles.py
│   │   │   ├── filters
│   │   │   │   ├── __init__.py
│   │   │   │   └── profiles.py
│   │   │   ├── __init__.py
│   │   │   ├── models
│   │   │   │   ├── __init__.py
│   │   │   │   └── profiles.py
│   │   │   └── services
│   │   │       ├── __init__.py
│   │   │       └── profiles.py
│   │   ├── users
│   │   │   ├── admin.py
│   │   │   ├── apps.py
│   │   │   ├── entities.py
│   │   │   ├── __init__.py
│   │   │   └── models.py
│   │   └── vacancies
│   │       ├── admin.py
│   │       ├── apps.py
│   │       ├── converters
│   │       │   ├── __init__.py
│   │       │   └── vacancies.py
│   │       ├── entities
│   │       │   ├── __init__.py
│   │       │   └── vacancies.py
│   │       ├── filters
│   │       │   ├── __init__.py
│   │       │   └── vacancies.py
│   │       ├── __init__.py
│   │       ├── models
│   │       │   ├── __init__.py
│   │       │   └── vacancies.py
│   │       └── services
│   │           ├── __init__.py
│   │           └── vacancies.py
│   ├── common
│   │   ├── converters
│   │   │   ├── base.py
│   │   │   ├── exceptions.py
│   │   │   └── __init__.py
│   │   ├── filters
│   │   │   └── pagination.py
│   │   ├── __init__.py
│   │   ├── models
│   │   │   ├── base.py
│   │   │   └── __init__.py
│   │   ├── services
│   │   │   ├── base.py
│   │   │   ├── __init__.py
│   │   │   └── notifications.py
│   │   └── utils
│   │       ├── __init__.py
│   │       └── time.py
│   ├── core
│   │   ├── asgi.py
│   │   ├── __init__.py
│   │   ├── settings
│   │   │   ├── base.py
│   │   │   ├── __init__.py
│   │   │   ├── local.py
│   │   │   └── prod.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   └── db.sqlite3
└── tests
    ├── __init__.py
    └── services
        ├── conftest.py
        ├── __init__.py
        └── test_vacancies.py
```
