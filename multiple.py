#!/usr/bin/python3

import aiohttp
import asyncio


async def get_async(url):
    async with aiohttp.ClientSession() as session:
        return await session.get(url)


urls = ['http://webcode.me', 'https://httpbin.org/get',
    'https://google.com', 'https://stackoverflow.com',
    'https://github.com']


async def launch():
    """Lanzadera lanzable asincrona que pide como un pobre"""
    
    resps = await asyncio.gather(*map(get_async, urls)) # -> TODO: entender porque esta esa *
    data = [resp.status for resp in resps]

    for status_code in data:
        print(status_code)

asyncio.run(launch())