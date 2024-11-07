#!/usr/bin/python3

import aiohttp
import asyncio

url = 'http://webcode.me'

async def main():
    """Mi primrea corrutina en python"""
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:

            print("Status:", response.status)

            data = await response.text()
            print(data)

asyncloopEvent = asyncio.new_event_loop()
asyncio.set_event_loop(asyncloopEvent)
#asyncio.set_event_loop(asyncio.new_event_loop()) ############################# podemos resumir las anteriores dos lineas en una

asyncloopEvent.run_until_complete(main())