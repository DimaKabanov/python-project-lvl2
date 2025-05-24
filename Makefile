install:
	uv sync

build:
	uv build

package-install:
	uv tool install --force dist/*.whl

lint:
	uv run ruff check --fix gendiff
	uv run ruff check --fix tests

test:
	uv run pytest