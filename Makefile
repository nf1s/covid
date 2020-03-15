test:
	poetry run pytest tests.py

test-coverage:
	poetry run coverage run -m pytest tests.py
	poetry run coverage report

deploy:
	poetry run python setup.py sdist
	poetry run twine upload dist/*

install:
	poetry install
