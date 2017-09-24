import time
import asyncio
import aiofiles
import aiohttp

URI = 'https://api.bf4stats.com/api/onlinePlayers?output=json'
MAX_CLIENTS = 500


async def fetch_async(pid):
    print('Fetch async process {} started'.format(pid))
    start = time.time()
    response = await aiohttp.request('GET', URI)
    datetime = response.headers.get('Date')
    response.close()
    async with aiofiles.open(str(pid) + '.out', mode='w') as f:
        await f.write(datetime)
    print('Process {}: {}, took: {:.2f} seconds'.format(
        pid, datetime, time.time() - start))
    return datetime


async def asynchronous():
    start = time.time()
    # Ensure future creates an event loop for us instead of doing asyncio.get_event_loop()
    tasks = [asyncio.ensure_future(fetch_async(i)) for i in range(1, MAX_CLIENTS + 1)]
    await asyncio.wait(tasks)
    print("TOTAL TIME TAKEN : {:.2f} seconds".format(time.time() - start))

print('Fetching urls concurrently : \n')
ioloop = asyncio.get_event_loop()
ioloop.run_until_complete(asynchronous())
ioloop.close()
