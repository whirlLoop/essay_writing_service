SHELL := /bin/bash

help:
	@$(MAKE) -pRrq -f $(lastword $(MAKEFILE_LIST)) : 2>/dev/null | awk -v RS= -F: '/^# File/,/^# Finished Make data base/ {if ($$1 !~ "^[#.]") {print $$1}}' | sort | egrep -v -e '^[^[:alnum:]]' -e '^$@$$'

install:
	pipenv install

activate:
	pipenv shell

run:
	source dev.env; python src/core/manage.py runserver;

migration:
	export DJANGO_SETTINGS_MODULE='core.settings.development'; export SECRET_KEY='secret key'; python src/core/manage.py makemigrations

migrate:
	export DJANGO_SETTINGS_MODULE='core.settings.development'; export SECRET_KEY='secret key'; python src/core/manage.py migrate

superuser:
	export DJANGO_SETTINGS_MODULE='core.settings.development'; export SECRET_KEY='secret key'; python src/core/manage.py createsuperuser

dev:
	docker-compose up --build --force-recreate --remove-orphans --detach

tear-dev:
	docker-compose down

clean:
	find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf

## Run tests. You can specify tests on a particular domain e.g. make test frontend
test:
	${INFO} "Testing $(TAG_ARGS)..."
	docker-compose run writing_service python src/core/manage.py test $(TAG_ARGS)

ifeq (test,$(firstword $(MAKECMDGOALS)))
  TAG_ARGS := $(word 2, $(MAKECMDGOALS))
  $(eval $(TAG_ARGS):;@:)
endif

# COLORS
YELLOW := `tput setaf 3`
NC := "\e[0m"

INFO := @bash -c 'printf $(YELLOW); echo "===> $$1"; printf $(NC)' SOME_VALUE