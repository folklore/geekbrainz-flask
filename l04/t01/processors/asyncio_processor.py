import asyncio
import aiohttp
import aiofiles
import time

import os
from urllib.parse import urlparse

async def download(url, i):
  start_at = time.time()

  async with aiohttp.ClientSession() as session:
    async with session.get(url) as response:
      filename = os.path.basename(urlparse(url).path)

      async with aiofiles.open(filename, mode='wb') as file:
        await file.write(await response.read())

      print(i, url, round(time.time() - start_at, 3))


async def main(urls):
  tasks = []
  for index, url in enumerate(urls):
    t = asyncio.create_task(download(url, index))
    tasks.append(t)
  await asyncio.gather(*tasks)


def call(urls):
  start_at = time.time()
  asyncio.run(main(urls))
  return round(time.time() - start_at, 3)
