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
{
    "method": "GET",
    "ordered": true,
    "urls": [
        "https://google.com",
        "https://yandex.ru",
        "https://httpbin.org/json"
    ]
}
```

Response contains of a unique ID that should be used to retrieve the result of the request.

```
719a6635-a90e-4e82-9e02-ddd7cb5a3cbf
```

#### Subscribe to responses

When in progress of fetching requested URLs, you can subscribe to the stream
of responses (newline separated JSON-list):

```
GET https://multiserver.ssl2.ru/<response-id>
```

Response content example:

```json
{"url": "https://google.com", "response": "<!doctype html><html itemscope=\"\"<...>"}
{"url": "https://yandex.ru", "response": "<!DOCTYPE html><html class=\"i-ua_js_<...>"}
{"url": "https://httpbin.org/json", "response": "{\n  \"slideshow\": {\n<...>"}
```
