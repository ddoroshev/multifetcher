<div align="center">
    <img src="img/multifetcher.svg" width="400px" alt="multifetcher"/>
</div>

Multifetcher is a simple web-based server that allows parallel requests to external resources.

## Usage

### API

#### Send request

```
POST https://multiserver.ssl2.ru/
```

JSON body:

```json
[
    {"method": "GET", "url": "https://google.com"}
    {"method": "GET", "headers": {"Cookie": "foo=bar"}, "url": "https://yandex.ru"}
    {"method": "GET", "headers": {"Foo": "Bar"}, "url": "https://httpbin.org/json"}
]
```

The response is a stream of newline separated JSON-list. Example:

```json
{"url": "https://google.com", "response": "<!doctype html><html itemscope=\"\"<...>"}
{"url": "https://yandex.ru", "response": "<!DOCTYPE html><html class=\"i-ua_js_<...>"}
{"url": "https://httpbin.org/json", "response": "{\n  \"slideshow\": {\n<...>"}
```
