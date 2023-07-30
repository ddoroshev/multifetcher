<div align="center">
    <img src="img/multifetcher.svg" width="400px" alt="multifetcher"/>
</div>

Multifetcher is a simple web-based server that allows parallel requests to external resources.

## Usage

### Build and run

```bash
docker build -t multifetcher .
docker run -d -p 8000:8000 multifetcher
```

### Send requests

```
POST http://localhost:8000/
```

JSON body:

```json
[
    {
        "id": "1",
        "method": "GET",
        "url": "https://google.com"
    },
    {
        "id": "2",
        "method": "GET",
        "headers": {"Cookie": "foo=bar"},
        "url": "https://yandex.ru"
    },
    {
        "id": "3",
        "method": "GET",
        "headers": {"Foo": "Bar"},
        "url": "https://httpbin.org/json"
    }
]
```

The response is a stream of newline separated JSON-list. Example:

```json
{"id": "1", "url": "https://google.com", "response": "<!doctype html><html itemscope=\"\"<...>"}
{"id": "2", "url": "https://yandex.ru", "response": "<!DOCTYPE html><html class=\"i-ua_js_<...>"}
{"id": "3", "url": "https://httpbin.org/json", "response": "{\n  \"slideshow\": {\n<...>"}
```
