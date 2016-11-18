PROJECT_DIR=$(shell pwd)
VENV_DIR?=$(PROJECT_DIR)/.env
PIP?=$(VENV_DIR)/bin/pip3
PYTHON?=$(VENV_DIR)/bin/python
MANAGE?=$(PROJECT_DIR)/manage.py
NOSE?=$(VENV_DIR)/bin/nosetests

.PHONY: all clean test run requirements install virtualenv


all: clean virtualenv install test create_database loaddata create_admin collect_static

virtualenv:
	virtualenv -p python3.5 $(VENV_DIR) --no-site-packages

install: requirements

requirements:
	$(PIP) install -r $(PROJECT_DIR)/requirements.txt


create_database:
	$(PYTHON) manage.py migrate
	$(PYTHON) manage.py migrate --noinput

create_admin:
	echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@site.com', '12345')" | $(PYTHON) manage.py shell

run:
	$(PYTHON) manage.py runserver

migrations:
	$(PYTHON) $(MANAGE) makemigrations $(app)

migrate:
	$(PYTHON) manage.py migrate

collect:
	$(PYTHON) manage.py collectstatic

shell:
	$(PYTHON) manage.py shell

test:
	$(PYTHON) manage.py test src/apps --verbosity=1 --logging-level=ERROR

clean_temp:
	find . -name '*.pyc' -delete
	rm -rf .coverage dist docs/_build htmlcov MANIFEST

clean_venv:
	rm -rf $(VENV_DIR)

clean: clean_temp clean_venv

