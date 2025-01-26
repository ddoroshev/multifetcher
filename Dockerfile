FROM ghcr.io/ddoroshev/pybase:3.13.1-compile-v1 as compile

COPY poetry.lock pyproject.toml /app/

RUN poetry install --no-root --only main

COPY . /app/


FROM ghcr.io/ddoroshev/pybase:3.13.1-runtime-v1 as runtime

COPY --from=compile /venv /venv
COPY --from=compile /app /app

EXPOSE 8000

CMD ["gunicorn", "multifetcher.main:app", "--bind", ":8000", "--worker-class", "aiohttp.GunicornUVLoopWebWorker", "--access-logfile", "-", "--error-logfile", "-"]
