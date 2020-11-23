install:
	pip install -e .

install-ci:
	pip install -e .\[ci\]

black:
	python -m black .

lint:
	python -m pylint app

test:
	python -m pytest tests

ci:
	make black
	make lint
	make test
	coveralls

migrate:
	alembic upgrade head
