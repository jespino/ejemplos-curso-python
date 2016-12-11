import asyncio
import async_timeout
import aiohttp
import os
from urls import *

async def fetch(session, url):
    with async_timeout.timeout(10):
        async with session.get(url) as response:
            return await response.text()


async def download_url_into_file(loop, filename, url):
    with aiohttp.ClientSession(loop=loop) as session:
        html = await fetch(session, 'http://python.org')
        fd = open(os.path.join("asyncio", filename), "w")
        fd.write(html)
        fd.close()


async def download_urls(loop):
    jobs = []
    for name, url in urls.items():
        filename = "%s.html" % name
        jobs.append(download_url_into_file(loop, filename, url))
    await asyncio.wait(jobs)

loop = asyncio.get_event_loop()
# Blocking call which returns when the display_date() coroutine is done
loop.run_until_complete(download_urls(loop))
loop.close()

print("Finish!")
