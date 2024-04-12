EXEC = docker exec -it
MANAGE_PY = python manage.py
APP = jobboard-app-1


.PHONY: migrate
migrate:
	${EXEC} ${APP} ${MANAGE_PY} migrate

.PHONY: superuser
superuser:
	${EXEC} ${APP} ${MANAGE_PY} createsuperuser
