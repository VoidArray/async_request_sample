import aiohttp
import asyncio

URLS = [
    'http://127.0.0.1:8000/json1/',
    'http://127.0.0.1:8000/json2/',
    'http://127.0.0.1:8000/json3/',
]

        
async def fetch(client, url):
    try:
        async with client.get(url, timeout=2) as resp:
            return await resp.json()
    except asyncio.TimeoutError:
        return {}

        
async def main(loop):
    async with aiohttp.ClientSession(loop=loop) as client:
        reqs = [fetch(client, url) for url in URLS]
        results = await asyncio.gather(*reqs)
        common_result = []
        for r in results:
            common_result.extend(r)

        common_answer = {(int(row['id']), row['name']) for row in common_result}
        common_answer_sorted = sorted(common_answer, key=lambda k: int(k[0]))
        print('#################')
        print('answer:')
        for c in common_answer_sorted:
            print(c[1])
        print('#################')


loop = asyncio.get_event_loop()
loop.run_until_complete(main(loop))
