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
**Every package has init file**
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
│   │   ├── schemas.py
│   │   ├── urls.py
│   │   └── v1
│   │       ├── profiles
│   │       │   ├── employers
│   │       │   │   ├── handlers.py
│   │       │   │   └── schemas.py
│   │       │   └── jobseekers
│   │       │       ├── handlers.py
│   │       │       └── schemas.py
│   │       └── vacancies
│   │           ├── handlers.py
│   │           └── schemas.py
│   ├── apps
│   │   ├── profiles
│   │   │   ├── admin.py
│   │   │   ├── apps.py
│   │   │   ├── converters
│   │   │   │   ├── employers.py
│   │   │   │   └── jobseekers.py
│   │   │   ├── entities
│   │   │   │   ├── base.py
│   │   │   │   ├── employers.py
│   │   │   │   └── jobseekers.py
│   │   │   ├── filters.py
│   │   │   ├── models
│   │   │   │   ├── base.py
│   │   │   │   ├── employers.py
│   │   │   │   └── jobseekers.py
│   │   │   └── services
│   │   │       ├── base.py
│   │   │       ├── employers.py
│   │   │       └── jobseekers.py
│   │   ├── users
│   │   │   ├── admin.py
│   │   │   ├── apps.py
│   │   │   ├── entities.py
│   │   │   ├── exceptions.py
│   │   │   ├── models.py
│   │   │   └── services
│   │   │       └── user.py
│   │   └── vacancies
│   │       ├── admin.py
│   │       ├── apps.py
│   │       ├── converters.py
│   │       ├── entities.py
│   │       ├── filters.py
│   │       ├── models.py
│   │       ├── services
│   │       │   ├── base.py
│   │       │   └── vacancies.py
│   │       └── use_cases
│   │           ├── base.py
│   │           └── vacancies.py
│   ├── common
│   │   ├── container.py
│   │   ├── converters
│   │   │   ├── base.py
│   │   │   └── exceptions.py
│   │   ├── filters
│   │   │   └── pagination.py
│   │   ├── models
│   │   │   └── base.py
│   │   ├── services
│   │   │   ├── base.py
│   │   │   ├── notifications.py
│   │   │   └── tasks.py
│   │   ├── use_cases
│   │   │   └── base.py
│   │   └── utils
│   │       └── time.py
│   └── core
│       ├── asgi.py
│       ├── celery.py
│       ├── settings
│       │   ├── base.py
│       │   ├── local.py
│       │   └── prod.py
│       ├── urls.py
│       └── wsgi.py
└── tests
    └── services
        ├── conftest.py
        └── test_vacancies.py

```
Boilerplate: https://github.com/greedWizard/django-docker-compose-postgres-boilerplate
