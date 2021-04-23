FROM python:3.9

RUN pip install poetry

COPY pyproject.toml poetry.lock /usr/src/app/

WORKDIR /usr/src/app

RUN poetry install --no-root --no-dev
