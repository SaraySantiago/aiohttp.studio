#!/usr/bin/python3

import aiohttp
import asyncio


async def get_async(url):
    async with aiohttp.ClientSession() as session:
        return await session.get(url)


urls = ['http://webcode.me', 'https://httpbin.org/get',
    'https://google.com','https://tusalchichonfavorito.com',
    'https://stackoverflow.com',
    'https://github.com']


async def launch():
    """Lanzadera lanzable asincrona que pide como un pobre"""
    #TODO: intentar poner un try// except -> ante una url inexistente
    #try:
    resps = await asyncio.gather(*map(get_async, urls)) # -> TODO: entender porque esta esa *
    stat = [resp.status for resp in resps]
    #except #socket,gaierror
    #except #ClientConnectorError 

    for status_code in stat:
        print(status_code)

asyncio.run(launch())