import json
import asyncio
from aiohttp import web, ClientSession

async def make_request(params, *, session, response):
    async with session.get(params['url']) as resp:
        resp_data = await resp.text()
        result = {'url': params['url'], 'response': resp_data}
        await response.write((json.dumps(result) + '\n').encode())

async def requester(request):
    response = web.StreamResponse()
    await response.prepare(request)
    tasks = []
    async with ClientSession() as session:
        for params in await request.json():
            task = asyncio.ensure_future(make_request(params, session=session, response=response))
            tasks.append(task)
        await asyncio.gather(*tasks)
    await response.write_eof()
    return response

app = web.Application()
app.add_routes([web.post('/', requester)])

if __name__ == '__main__':
    web.run_app(app)
