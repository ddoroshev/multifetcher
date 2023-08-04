<div align="center">
    <img src="img/multifetcher.svg" width="400px" alt="multifetcher"/>
</div>

Multifetcher is a web-based server that enables parallel requests to external resources. This lightweight, high-performance solution takes advantage of Python's asynchronous I/O capabilities to fetch data from multiple URLs concurrently and efficiently.

## Features
- Asynchronous HTTP requests to external resources
- Dockerized application for easy setup and isolation
- HTTP POST API to receive multiple request details
- Streamed responses for real-time results
- Timeout handling for each request

## Getting Started

These instructions will get you a copy of the project up and running on your local machine.

### Prerequisites

- Docker

### Installation & Running

1. Clone this repository:

```bash
git clone https://github.com/yourusername/multifetcher.git
cd multifetcher
```

2. Build the Docker image:

```bash
docker build -t multifetcher .
```

3. Run the Docker container:

```bash
docker run -d -p 8000:8000 multifetcher
```

The server is now running at `http://localhost:8000`.

### Usage

Multifetcher listens for POST requests at its root URL. The body of the request should be a JSON array of objects representing the HTTP requests to make. An example POST request body might look like this:

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

The server responds with a stream of newline-separated JSON objects. Each object corresponds to a response from one of the HTTP requests:

```json
{"id": "1", "url": "https://google.com", "response": "<!doctype html><html itemscope=\"\"<...>"}
{"id": "2", "url": "https://yandex.ru", "response": "<!DOCTYPE html><html class=\"i-ua_js_<...>"}
{"id": "3", "url": "https://httpbin.org/json", "response": "{\n  \"slideshow\": {\n<...>"}
```

## Testing

You can test Multifetcher by running the provided `test.py` script:

```bash
python test.py
```

This script sends a series of test HTTP requests to the server and prints the responses.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
