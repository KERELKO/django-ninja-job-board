1. make authentication & authorization
2. make filters
3. build scalable project structure
4. to finish Makefile
5. Dockerfile, docker-compose
6. make tests
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
