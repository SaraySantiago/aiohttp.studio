#!/usr/bin/python

import aiohttp
import asyncio


async def get_async(url):
    async with aiohttp.ClientSession() as session:
        return await session.get(url)


urls = ['http://webcode.me', 'https://httpbin.org/get',
    'https://google.com', 'https://stackoverflow.com',
    'https://github.com']


async def launch():
    
    resps = await asyncio.gather(*map(get_async, urls))
    data = [resp.status for resp in resps]

    for status_code in data:
        print(status_code)

asyncio.run(launch())