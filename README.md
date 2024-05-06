# Django Job Board

Built with **Django**, **NinjaAPI**, **Celery**, **Rabbitmq**, **Redis** and **PostgreSQL**  
It provides common job board features such as filtering vacancies and filtering candidates who have applied for a vacancy to find the best match.   
Additionally it has flexible notification system that uses **Celery**.  

## Technologies Used

- [Django](https://www.djangoproject.com/) - High-level Python web framework that encourages rapid development and clean, pragmatic design.
- [NinjaAPI](https://django-ninja.dev/) - Powerful framework for building APIs in Django with flexible and fast development.
- [PostgreSQl](https://www.postgresql.org/) - Relational database management system
- [Docker](https://www.docker.com/) - Platform for developing, shipping, and running applications in containers.
- [Redis](https://redis.io/) - Fastest in-memory storage for caching
- [Celery](https://docs.celeryq.dev/en/stable/) - Simple, flexible, and reliable distributed system to process vast amounts of messages
- [RabbitMQ](https://www.rabbitmq.com/) - Reliable and mature messaging and streaming broker
## Installation
For installation of the project you required to have __Docker__ and __docker-compose__ tool installed on your machine,  
and for better usage experience: __Make tools__  
To install this project:

1. Clone this repository.
```
git clone https://github.com/KERELKO/Django-ninja-job-board
```
2. create __.env__ file based on **.env.example**
3. move to directory with __docker-compose.yaml__ and run:
```
docker compose up --build
```
4. The project provides several helpful Make commands, run
```
make migrate
```
the command responsible for applying and unapplying migrations

## Usage

Once the application is running, you can access the job board features through the __Swagger__  
Go to __http://127.0.0.1:8000/api/docs#/__ in your browser while project is running in docker and you will see:

![image](https://github.com/KERELKO/Django-ninja-job-board/assets/89779202/729725bf-6716-4cca-9e73-5e1aa2b1a5f3)

### Make commands
```
make mirgate  # make database migrations
make migrations  # applied databases changes 
make superuser  # make django superuser
make tests  # run all available tests
make shell  # open django shell in app container
make bash  # open terminal in app container
```
## Contributing

If you'd like to contribute to this project, feel free to fork the repository and submit a pull request. Please follow the existing code style and ensure that all tests pass before submitting your changes.

## Project structure

```
.
├── Dockerfile
├── Makefile
├── README.md
├── docker-compose.yaml
├── manage.py
├── poetry.lock
├── pyproject.toml
├── src
│   ├── api
│   │   ├── __init__.py
│   │   ├── schemas.py
│   │   ├── urls.py
│   │   └── v1
│   │       ├── __init__.py
│   │       ├── profiles
│   │       │   ├── __init__.py
│   │       │   ├── employers
│   │       │   │   ├── __init__.py
│   │       │   │   ├── handlers.py
│   │       │   │   └── schemas.py
│   │       │   └── jobseekers
│   │       │       ├── __init__.py
│   │       │       ├── handlers.py
│   │       │       └── schemas.py
│   │       └── vacancies
│   │           ├── __init__.py
│   │           ├── handlers.py
│   │           └── schemas.py
│   ├── apps
│   │   ├── __init__.py
│   │   ├── profiles
│   │   │   ├── __init__.py
│   │   │   ├── admin.py
│   │   │   ├── apps.py
│   │   │   ├── converters
│   │   │   │   ├── __init__.py
│   │   │   │   ├── employers.py
│   │   │   │   └── jobseekers.py
│   │   │   ├── entities
│   │   │   │   ├── __init__.py
│   │   │   │   ├── base.py
│   │   │   │   ├── employers.py
│   │   │   │   └── jobseekers.py
│   │   │   ├── filters.py
│   │   │   ├── models
│   │   │   │   ├── __init__.py
│   │   │   │   ├── base.py
│   │   │   │   ├── employers.py
│   │   │   │   └── jobseekers.py
│   │   │   ├── services
│   │   │   │   ├── __init__.py
│   │   │   │   ├── base.py
│   │   │   │   ├── employers.py
│   │   │   │   └── jobseekers.py
│   │   │   └── use_cases
│   │   │       └── jobseekers.py
│   │   ├── users
│   │   │   ├── __init__.py
│   │   │   ├── admin.py
│   │   │   ├── apps.py
│   │   │   ├── entities.py
│   │   │   ├── exceptions.py
│   │   │   ├── models.py
│   │   │   └── services
│   │   │       └── user.py
│   │   └── vacancies
│   │       ├── __init__.py
│   │       ├── admin.py
│   │       ├── apps.py
│   │       ├── converters.py
│   │       ├── entities.py
│   │       ├── filters.py
│   │       ├── models.py
│   │       ├── services
│   │       │   ├── __init__.py
│   │       │   ├── base.py
│   │       │   └── vacancies.py
│   │       └── use_cases
│   │           └── vacancies.py
│   ├── common
│   │   ├── __init__.py
│   │   ├── container.py
│   │   ├── converters
│   │   │   ├── __init__.py
│   │   │   ├── base.py
│   │   │   └── exceptions.py
│   │   ├── filters
│   │   │   ├── __init__.py
│   │   │   └── pagination.py
│   │   ├── models
│   │   │   ├── __init__.py
│   │   │   ├── base.py
│   │   │   └── exeptions.py
│   │   ├── services
│   │   │   ├── __init__.py
│   │   │   ├── base.py
│   │   │   ├── exceptions.py
│   │   │   └── notifications.py
│   │   └── utils
│   │       ├── __init__.py
│   │       ├── orm.py
│   │       └── time.py
│   ├── core
│   │   ├── __init__.py
│   │   ├── asgi.py
│   │   ├── celery.py
│   │   ├── exceptions.py
│   │   ├── init.py
│   │   ├── settings
│   │   │   ├── __init__.py
│   │   │   ├── base.py
│   │   │   ├── local.py
│   │   │   └── prod.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   └── db.sqlite3
└── tests
    ├── __init__.py
    └── services
        ├── __init__.py
        ├── conftest.py
        └── test_vacancies.py
```
TODO:
 - [ ] Make the structure more flexible by passing entities in use cases and services instead of ids
 - [ ] Cache the content
 - [ ] Cover more parts of the project with robust tests  
### The main structure of the project is taken from the repo below thanks to the author!
Boilerplate: https://github.com/greedWizard/django-docker-compose-postgres-boilerplate
