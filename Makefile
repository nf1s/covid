test:
	pipenv run pytest tests.py

test-coverage:
	pipenv run coverage run -m pytest tests.py
	pipenv run coverage report

deploy:
	pipenv run python setup.py sdist
	pipenv run twine upload dist/*

install:
	pipenv install

docs:
	mkdocs gh-deploy
