.PHONY: install run

install:
	poetry install

run:
	poetry run fastapi dev src/oracle/main.py

docker-run:
	docker compose up --build
