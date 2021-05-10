import asyncio
import threading
import time

import httpx

client = httpx.AsyncClient()


async def async_main(url, sign):  #
    response = await client.get(url)
    status_code = response.status_code
    print(f"async_main: {threading.current_thread()}: {sign}: {status_code}")



# loop = asyncio.new_event_loop()
loop = asyncio.get_event_loop()
tasks = [async_main(url='http://www.baidu.com', sign=i) for i in range(20)]
async_start = time.time()
loop.run_until_complete(asyncio.wait(tasks))
async_end = time.time()
loop.close()
print(async_end - async_start)
