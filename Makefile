EXEC = docker exec -it
APP = jobboard-app-1

.PHONY: migrate
migrate:
	${EXEC} ${APP} python manage.py migrate
