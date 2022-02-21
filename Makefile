check-pep257:
	@prospector --with-tool pep257

freeze:
	@pip freeze

format:
	@blue .
	@isort .

install-requirements:
	@pip install -r ./requirements/base.txt
	@pip install -r ./requirements/test.txt

lint:
	@blue . --check
	@isort . --check

test:
	@pytest -s