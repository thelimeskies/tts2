.PHONY: build clean down up shell migrate bootstrap

build:
	docker-compose -f local.yml build

clean:  clean-pyc
				docker compose -f local.yml down -v --remove-orphans
				docker compose -f local.yml down -v --remove-orphans

clean-pyc:
				sudo find . -name '*.pyc' -exec rm -f {} +
				sudo find . -name '*.pyo' -exec rm -f {} +
				sudo find . -name '*~' -exec rm -f {} +
				sudo find . -name '__pycache__' -exec rm -fr {} +
				sudo rm -fr src/.ipython

down:
				docker compose -f local.yml down --remove-orphans
				docker compose -f local.yml down --remove-orphans

up: down
				docker compose -f local.yml up

dev-up: down
				docker compose -f local.yml up -d postgres mailhog redis celeryworker celerybeat flower

django:
				docker compose -f local.yml rm -s -v django
				docker compose -f local.yml up django

shell:
				docker compose -f local.yml run --rm django python manage.py shell

bash:
				docker compose -f local.yml run --rm django /bin/bash

dbshell:
				docker compose -f local.yml run --rm django python manage.py dbshell

migrate:
				docker compose -f local.yml run --rm django python manage.py migrate

migrate-to:
				docker compose -f local.yml run --rm django python manage.py migrate $(app) $(migration)

migrations:
				docker compose -f local.yml run --rm django python manage.py makemigrations
