.PHONY: install run

install:
	poetry install

run:
	poetry run python ./src/oracle/main.py
