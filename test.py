import json
from pprint import pprint

import requests

TEST_PARAMS = [
    {"id": "first_one", "method": "GET", "url": "https://google.com", "timeout": 1},
    {
        "id": 234,
        "method": "GET",
        "headers": {"Cookie": "foo=bar"},
        "url": "https://yandex.ru",
        "timeout": 2,
    },
    {
        "id": "unagi",
        "method": "POST",
        "headers": {"Foo": "Bar"},
        "url": "https://httpbin.org/post",
        "json": {"Boom": "Wow"},
        "timeout": 3,
    },
    {
        "method": "POST",
        "headers": {"Foo": "Bar"},
        "url": "https://httpbin.org/post",
        "json": {"Boom": "Wow"},
        "timeout": 4,
    },
    {
        "method": "POST",
        "headers": {"Foo": "Bar"},
        "url": "https://httpbin.org/post",
        "json": {"Boom": "Wow"},
        "timeout": 0,
    },
    {
        "method": "POST",
        "headers": {"Foo": "Bar"},
        "url": "https://httpbin.org/post",
        "json": {"Boom": "Wow"},
        "timeout": 1,
    },
]

RESPONSE_LENGTH = 150


def run():
    resp = requests.post("http://localhost:8000/", json=TEST_PARAMS, stream=True)
    for line in resp.iter_lines():
        data = json.loads(line.decode())
        response = data["response"]
        if len(response) > RESPONSE_LENGTH:
            data["response"] = response[:RESPONSE_LENGTH] + "..."
        pprint(data)


if __name__ == "__main__":
    run()
