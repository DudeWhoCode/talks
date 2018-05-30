import time
import requests
import asyncio
import aiohttp

URL = 'https://api.bf4stats.com/api/onlinePlayers?output=json'
SUM_REQ = 3


def make_http_call_sync(pid):
    """ Make a GET request to the URL and get Date field from metadata, synchronously!"""
    print('Fetch sync process {} started'.format(pid))
    start = time.time()
    r = requests.get(URL)
    server_info = r.headers['Server']
    print('Process {}: {}, took: {:.2f} seconds'.format(
        pid, server_info, time.time() - start))

    return server_info


async def make_http_call_async(pid):
    """ Make a GET request to the URL and get Date field from metadata, asynchronously!"""
    print('Fetch async process {} started'.format(pid))
    start = time.time()

    # On await, While waiting for response each request yields the control flow to event loop
    response = await aiohttp.request('GET', URL)
    server_info = response.headers.get('Server')

    print('Process {}: {}, took: {:.2f} seconds'.format(
        pid, server_info, time.time() - start))

    response.close()
    return server_info


def synchronous():
    """ Initialize synchronous task"""
    start = time.time()
    for i in range(1, SUM_REQ + 1):
        make_http_call_sync(i)
    print("Process took: {:.2f} seconds".format(time.time() - start))


async def asynchronous():
    """ Initialize asynchronous task"""
    start = time.time()

    tasks = []
    for i in range(1, SUM_REQ + 1):
        task = make_http_call_async(i)
        tasks.append(task)

    await asyncio.wait(tasks)
    print("Total process took: {:.2f} seconds".format(time.time() - start))


# Kick off synchronous task
print('Synchronous:')
synchronous()

# Kick off asynchronous task
print('Asynchronous:')
ioloop = asyncio.get_event_loop()
ioloop.run_until_complete(asynchronous())
ioloop.close()
