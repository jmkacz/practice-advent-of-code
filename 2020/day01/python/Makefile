.PHONY: all
all: clean install test

clean:
	rm -rf .mypy_cache
	rm -rf .pytest_cache
	find . -type d -depth -name __pycache__ -exec rm -rf "{}" \;

install:
	poetry update
	poetry install

test:
	poetry run py.test -vv .

t1:
	poetry run py.test -vv tests/test_part1.py

t2:
	poetry run py.test -vv tests/test_part2.py

format:
	poetry run black .

mypy:
	poetry run mypy .
