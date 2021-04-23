FROM python:3.9

RUN pip install poetry

COPY pyproject.toml /usr/src/app

WORKDIR /usr/src/app

RUN pip