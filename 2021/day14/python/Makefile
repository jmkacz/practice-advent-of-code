.PHONY: all

VENV=${HOME}/.virtualenvs/advent

all: clean install test

clean:
	rm -rf .mypy_cache
	rm -rf .pytest_cache
	find . -type d -depth -name __pycache__ -exec rm -rf "{}" \;

install:
	python -m venv $(VENV)
	$(VENV)/bin/python -m pip install -r ../../requirements.txt
	$(VENV)/bin/python -m pip install --upgrade pip

test:
	$(VENV)/bin/py.test -vv .

t1:
	$(VENV)/bin/py.test -vv test_part1.py

t2:
	$(VENV)/bin/py.test -vv test_part2.py

format:
	$(VENV)/bin/black .

mypy:
	$(VENV)/bin/mypy .
