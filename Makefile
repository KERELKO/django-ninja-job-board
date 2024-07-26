EXEC = docker exec -it
MANAGE_PY = python manage.py
APP = app

.PHONY: logs
logs:
	docker logs ${APP}

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

.PHONY: tests
tests:
	${EXEC} ${APP} pytest tests/
