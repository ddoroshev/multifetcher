import asyncio
from aiohttp import web

async def requester(request):
    response = web.StreamResponse()
    await response.prepare(request)
    for i in range(100):
        print(i)
        await response.write(str(i).encode() + b'\n')
        await asyncio.sleep(1)
    await response.write_eof()
    return response

app = web.Application()
app.add_routes([web.post('/', requester)])

if __name__ == '__main__':
    web.run_app(app)
