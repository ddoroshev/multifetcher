FROM ghcr.io/ddoroshev/pybase:compile-3.12.3 as compile

COPY poetry.lock pyproject.toml /app/

RUN poetry install --no-root --only main

COPY . /app/


FROM ghcr.io/ddoroshev/pybase:runtime-3.12.3 as runtime

COPY --from=compile /venv /venv
COPY --from=compile /app /app

EXPOSE 8000

CMD ["gunicorn", "multifetcher.main:app", "--bind", ":8000", "--worker-class", "aiohttp.GunicornUVLoopWebWorker", "--access-logfile", "-", "--error-logfile", "-"]
