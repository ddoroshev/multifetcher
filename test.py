import requests
import json

TEST_PARAMS = [
    {"method": "GET", "url": "https://google.com"},
    {"method": "GET", "headers": {"Cookie": "foo=bar"}, "url": "https://yandex.ru"},
    {"method": "GET", "headers": {"Foo": "Bar"}, "url": "https://httpbin.org/json"}
]

def run():
    resp = requests.post('http://localhost:8000/', json=TEST_PARAMS, stream=True)
    for line in resp.iter_lines():
        print('###', json.loads(line.decode()))

if __name__ == '__main__':
    run()
