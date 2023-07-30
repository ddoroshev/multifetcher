import argparse
import asyncio
import json
from uuid import uuid4

from aiohttp import ClientTimeout, client, web

DEFAULT_TIMEOUT = 2
MAX_TIMEOUT = 10


async def make_request(params, *, response):
    timeout = max(params.get("timeout", DEFAULT_TIMEOUT), MAX_TIMEOUT)
    result = {
        "id": params.get("id", str(uuid4())),
        "url": params["url"],
    }
    try:
        async with client.request(
            params["method"],
            params["url"],
            headers=params.get("headers"),
            data=params.get("data"),
            json=params.get("json"),
            timeout=ClientTimeout(total=timeout),
        ) as resp:
            resp_data = await resp.text()
            result["response"] = resp_data
    except TimeoutError:
        result.update(
            {
                "response": "",
                "error": "Timeout",
            }
        )

    await response.write((json.dumps(result) + "\n").encode())


async def requester(request):
    response = web.StreamResponse()
    await response.prepare(request)
    tasks = []
    for params in await request.json():
        task = asyncio.ensure_future(make_request(params, response=response))
        tasks.append(task)
    await asyncio.gather(*tasks)
    await response.write_eof()
    return response


parser = argparse.ArgumentParser(description="Multifetcher")
parser.add_argument('--host', default="127.0.0.1")
parser.add_argument('--port', default="8000")

app = web.Application()
app.add_routes([web.post("/", requester)])

if __name__ == "__main__":
    args = parser.parse_args()
    web.run_app(app, host=args.host, port=args.port)
