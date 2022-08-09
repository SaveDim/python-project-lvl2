install:
	poetry install

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=hexlet_code --cov-report xml

lint:
	poetry run flake8 hexlet_code

selfcheck:
	poetry check

check: selfcheck test lint

build: check
	poetry build

package-install:
    python3 -m pip install --upgrade --force-reinstall dist/hexlet_code-0.2.0-py3-none-any.whl

.PHONY: install test lint selfcheck check build