#!/usr/bin/python

import aiohttp
import asyncio

url = 'http://webcode.me'

async def main():

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:

            print("Status:", response.status)

            data = await response.text()
            print(data)

loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
loop.run_until_complete(main())