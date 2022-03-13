check-pep257:
	@prospector --with-tool pep257

check-pep8:
	@prospector -F

freeze:
	@pip freeze

format:
	@blue .
	@isort .

install-requirements:
	@pip install -r ./requirements/base.txt
	@pip install -r ./requirements/test.txt

update-requirements:
	@rm ./requirements/base.txt
	@rm ./requirements/test.txt
	@pip-compile ./requirements/base.in
	@pip-compile ./requirements/test.in

lint:
	@blue . --check
	@isort . --check

test:
	@pytest -s

run:
	@python ./src/manage.py runserver

create-migrate:
	@python ./src/manage.py makemigrations

run-migrate:
	@python ./src/manage.py migrate

pre-commit:
	@pre-commit run --all-files
