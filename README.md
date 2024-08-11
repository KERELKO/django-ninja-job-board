# Django Job Board

Built with **Django**, **NinjaAPI**, **Celery**, **Rabbitmq**, **Redis** and **PostgreSQL**  
It provides common job board features such as filtering vacancies and filtering candidates who have applied for a vacancy to find the best match.   
Additionally it has flexible notification system that uses **Celery**.  

## Technologies Used

- [Django](https://www.djangoproject.com/) - High-level Python web framework that encourages rapid development and clean design
- [NinjaAPI](https://django-ninja.dev/) - Powerful framework for building APIs in Django with flexible and fast development
- [PostgreSQL](https://www.postgresql.org/) - Relational database management system
- [Docker](https://www.docker.com/) - Platform for developing, shipping, and running applications in containers
- [Redis](https://redis.io/) - Fastest in-memory storage, great for caching
- [Celery](https://docs.celeryq.dev/en/stable/) - Simple, flexible, and reliable distributed system to process vast amounts of messages
- [RabbitMQ](https://www.rabbitmq.com/) - Reliable and mature messaging and streaming broker
## Installation
For installation of the project you required to have __Docker__ and __docker-compose__ installed on your machine,  
and for better usage experience: __Make tools__  
To install this project:

1. Clone this repository.
```
git clone https://github.com/KERELKO/Django-ninja-job-board
```
2. move to directory with __.env.example__ and create __.env__ file based on **.env.example**
3. in the same directory run:
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
make migrate  # applies database migrations (manage.py migrate)
make migrations  # creates migrations (manage.py makemigrations) 
make superuser  # make django superuser (manage.py createsuperuser)
make tests  # run all available tests (pytest tests/)
make shell  # open django shell in app container (python manage.py shell)
make bash  # open terminal in app container
```
## Contributing

If you'd like to contribute to this project, feel free to fork the repository and submit a pull request. Please follow the existing code style and ensure that all tests pass before submitting your changes.

## Project structure

```
.
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
│   │       │   │   ├── handlers.py
│   │       │   │   ├── __init__.py
│   │       │   │   └── schemas.py
│   │       │   ├── __init__.py
│   │       │   └── jobseekers
│   │       │       ├── handlers.py
│   │       │       ├── __init__.py
│   │       │       └── schemas.py
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
│   │   │   │   ├── employers.py
│   │   │   │   ├── __init__.py
│   │   │   │   └── jobseekers.py
│   │   │   ├── entities
│   │   │   │   ├── base.py
│   │   │   │   ├── employers.py
│   │   │   │   ├── __init__.py
│   │   │   │   └── jobseekers.py
│   │   │   ├── filters.py
│   │   │   ├── __init__.py
│   │   │   ├── models
│   │   │   │   ├── base.py
│   │   │   │   ├── employers.py
│   │   │   │   ├── __init__.py
│   │   │   │   └── jobseekers.py
│   │   │   ├── services
│   │   │   │   ├── base.py
│   │   │   │   ├── employers.py
│   │   │   │   ├── __init__.py
│   │   │   │   └── jobseekers.py
│   │   │   └── use_cases
│   │   │       └── jobseekers.py
│   │   ├── users
│   │   │   ├── admin.py
│   │   │   ├── apps.py
│   │   │   ├── entities.py
│   │   │   ├── exceptions.py
│   │   │   ├── __init__.py
│   │   │   ├── models.py
│   │   │   └── services
│   │   │       └── user.py
│   │   └── vacancies
│   │       ├── admin.py
│   │       ├── apps.py
│   │       ├── converters.py
│   │       ├── entities.py
│   │       ├── enums.py
│   │       ├── filters.py
│   │       ├── __init__.py
│   │       ├── models.py
│   │       ├── services
│   │       │   ├── base.py
│   │       │   ├── __init__.py
│   │       │   └── vacancies.py
│   │       └── use_cases
│   │           └── vacancies.py
│   ├── common
│   │   ├── container.py
│   │   ├── converters
│   │   │   ├── base.py
│   │   │   ├── exceptions.py
│   │   │   └── __init__.py
│   │   ├── filters
│   │   │   ├── __init__.py
│   │   │   └── pagination.py
│   │   ├── __init__.py
│   │   ├── models
│   │   │   ├── base.py
│   │   │   ├── exeptions.py
│   │   │   └── __init__.py
│   │   ├── services
│   │   │   ├── base.py
│   │   │   ├── exceptions.py
│   │   │   ├── __init__.py
│   │   │   └── notifications.py
│   │   └── utils
│   │       ├── cache.py
│   │       ├── __init__.py
│   │       ├── orm.py
│   │       └── time.py
│   └── core
│       ├── asgi.py
│       ├── celery.py
│       ├── exceptions.py
│       ├── __init__.py
│       ├── init.py
│       ├── settings
│       │   ├── base.py
│       │   ├── __init__.py
│       │   ├── local.py
│       │   └── prod.py
│       ├── urls.py
│       └── wsgi.py
└── tests
    ├── api
    │   ├── conftest.py
    │   └── test_vacancy_handlers.py
    ├── fake
    │   └── services
    │       ├── __init__.py
    │       ├── jobseekers.py
    │       └── vacancies.py
    ├── __init__.py
    ├── services
    │   ├── conftest.py
    │   ├── test_common_services.py
    │   └── test_vacancy_service.py
    └── use_cases
        ├── conftest.py
        ├── test_jobseeker_use_cases.py
        └── test_vacancy_use_cases.py
```

TODO:
 - [ ] Make the structure more flexible by passing entities in use cases and services instead of ids
 - [X] Cache the content
 - [x] Cover more parts of the project with robust tests  
### The main structure of the project is taken from the repo below thanks to the author!
Boilerplate: https://github.com/greedWizard/django-docker-compose-postgres-boilerplate
