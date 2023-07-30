FROM python:3.11.4

RUN pip install poetry

COPY pyproject.toml poetry.lock /usr/src/app/

WORKDIR /usr/src/app

RUN poetry install --no-root --no-dev

# TODO(dima) Add port
CMD ["python", "-m", "multifetcher.main"]
