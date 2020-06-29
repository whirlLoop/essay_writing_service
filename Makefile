SHELL := /bin/bash

help:
	@$(MAKE) -pRrq -f $(lastword $(MAKEFILE_LIST)) : 2>/dev/null | awk -v RS= -F: '/^# File/,/^# Finished Make data base/ {if ($$1 !~ "^[#.]") {print $$1}}' | sort | egrep -v -e '^[^[:alnum:]]' -e '^$@$$'

install:
	pipenv install

activate:
	pipenv shell

run:
	export DJANGO_SETTINGS_MODULE='core.settings.development'; export SECRET_KEY='secret key'; python src/core/manage.py runserver

migration:
	export DJANGO_SETTINGS_MODULE='core.settings.development'; export SECRET_KEY='secret key'; python src/core/manage.py makemigrations

migrate:
	export DJANGO_SETTINGS_MODULE='core.settings.development'; export SECRET_KEY='secret key'; python src/core/manage.py migrate

superuser:
	export DJANGO_SETTINGS_MODULE='core.settings.development'; export SECRET_KEY='secret key'; python src/core/manage.py createsuperuser

deploy:
	docker-compose build
	docker-compose up -d

down:
	docker-compose down