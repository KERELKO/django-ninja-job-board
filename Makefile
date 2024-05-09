EXEC = docker exec -it
MANAGE_PY = python manage.py
APP = django-ninja-job-board-app-1


.PHONY: migrate
migrate:
	${EXEC} ${APP} ${MANAGE_PY} migrate

.PHONY: superuser
superuser:
	${EXEC} ${APP} ${MANAGE_PY} createsuperuser

.PHONY: migrations
migrations:
	${EXEC} ${APP} ${MANAGE_PY} makemigrations vacancies profiles users

.PHONY: shell
shell:
	${EXEC} ${APP} ${MANAGE_PY} shell

.PHONY: bash
bash:
	${EXEC} ${APP} bash

# Tests
.PHONY: tests
tests:
	${EXEC} ${APP} pytest tests/
