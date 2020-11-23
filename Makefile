install:
	pip install -e .\[dev\]

black:
	python -m black .

lint:
	python -m pylint code

test:
	python -m pytest tests

ci:
	make black
	make lint
	make test
