.PHONY: test test-coverage build publish setup deploy-docs serve-docs shell

test:
	@poetry run pytest

test-coverage:
	@poetry run coverage run -m pytest
	@poetry run coverage report

build:
	@poetry build

publish:
	@poetry publish --build

setup:
	@poetry install

deploy-docs:
	@poetry run mkdocs gh-deploy

serve-docs:
	@poetry run mkdocs serve

shell:
	@poetry run ipython
