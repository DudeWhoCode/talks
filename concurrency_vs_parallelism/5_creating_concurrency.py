import time
import random
import asyncio
import aiohttp

URL = 'https://api.bf4stats.com/api/onlinePlayers?output=json'
SUM_REQ = 3


async def make_http_call_async(pid):
    """ Make a GET request to the URL and get Date field from metadata, asynchronously!"""
    start = time.time()
    sleep_time = random.randint(2, 5)
    print('Parsing HTTP response process {} started, sleeping for {} seconds'.format(
        pid, sleep_time))

    await asyncio.sleep(sleep_time)

    response = await aiohttp.request('GET', URL)
    server_info = response.headers.get('Server')

    response.close()
    return 'Process {}: {}, took: {:.2f} seconds'.format(
        pid, server_info, time.time() - start)


async def asynchronous():
    """ Initialize asynchronous task"""
    start = time.time()
    tasks = [make_http_call_async(i) for i in range(1, SUM_REQ + 1)]

    # as_completed function returns an iterator that will yield a future as soon as it gets completed
    for i, future in enumerate(asyncio.as_completed(tasks)):
        result = await future
        print('{} {}'.format(">>" * (i + 1), result))

    print("Total process took: {:.2f} seconds".format(time.time() - start))


ioloop = asyncio.get_event_loop()
ioloop.run_until_complete(asynchronous())
ioloop.close()
