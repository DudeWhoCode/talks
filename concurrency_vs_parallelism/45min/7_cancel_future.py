import time
import asyncio
from concurrent.futures import FIRST_COMPLETED
import aiohttp

SERVICES = [{'name': 'ipify', 'url': 'https://api.ipify.org?format=json', 'ip_attr': 'ip'},
            {'name': 'ip-api', 'url': 'http://ip-api.com/json', 'ip_attr': 'query'}]


async def find_my_ip(service):
    """ Get current IP address by hitting 3rd party APIs"""
    start = time.time()
    print('Fetching IP from {}'.format(service['name']))

    response = await aiohttp.request('GET', service['url'])
    json_response = await response.json()
    ip = json_response[service['ip_attr']]

    response.close()
    return '{} finished with result: {}, took: {:.2f} seconds'.format(
        service['name'], ip, time.time() - start)


async def asynchronous():
    """ Initialize asynchronous task"""
    futures = [find_my_ip(service) for service in SERVICES]

    # Returns the future when first task gets completed
    done, pending = await asyncio.wait(
        futures, return_when=FIRST_COMPLETED)

    # States of the future: Pending, Running, Done, Cancelled
    for future in done:
        print('Future Done?: ', future.done())

    print(done.pop().result())

    # Cancel the pending future to avoid warnings, after getting first result
    for future in pending:
        print('Future Done?: ', future.done())
        future.cancel()

ioloop = asyncio.get_event_loop()
ioloop.run_until_complete(asynchronous())
ioloop.close()
