.PHONY: all

PYTHON_VERSION=3.11.0
VIRTUALENV_NAME=advent-of-code-2022

all: clean install test

clean:
	rm -rf .mypy_cache
	rm -rf .pytest_cache
	find . -type d -depth -name __pycache__ -exec rm -rf "{}" \;

install:
	( pyenv versions | sed 's/^..//' | awk '{ print $$1 }' | grep -q "^${VIRTUALENV_NAME}$$" ) || pyenv virtualenv ${PYTHON_VERSION} ${VIRTUALENV_NAME}
	pyenv local ${VIRTUALENV_NAME}
	python -m pip install --upgrade pip
	python -m pip install -r ../../requirements.txt

test:
	py.test -vv .

format:
	black .
	isort .

lint:
	pflake8 .
	pylint . --recursive=true
	mypy .
