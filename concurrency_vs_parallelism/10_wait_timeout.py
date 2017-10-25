import time
import random
import asyncio
import aiohttp
import argparse
from concurrent.futures import FIRST_COMPLETED

SERVICES = [{'name': 'ipify', 'url': 'https://api.ipify.org?format=json', 'ip_attr': 'ip'},
            {'name': 'ip-api', 'url': 'http://ip-api.com/json', 'ip_attr': 'query'}]
TIMEOUT = 0.5  # 3


async def find_my_ip(service):
    """ Get current IP address by hitting 3rd party APIs"""
    start = time.time()
    print('Fetching IP from {}'.format(service['name']))

    await asyncio.sleep(random.randint(1, 3) * 0.1)
    try:
        response = await aiohttp.request('GET', service['url'])
    except:
        return '{} is unresponsive'.format(service['name'])

    json_response = await response.json()
    ip = json_response[service['ip_attr']]

    response.close()
    print('{} finished with result: {}, took: {:.2f} seconds'.format(
        service['name'], ip, time.time() - start))
    return ip


async def asynchronous(timeout):
    """ Initialize asynchronous task"""
    response = {
        "message": "Result from asynchronous.",
        "ip": "not available"
    }

    futures = [find_my_ip(service) for service in SERVICES]
    done, pending = await asyncio.wait(
        futures, timeout=timeout, return_when=FIRST_COMPLETED)

    for future in pending:
        future.cancel()

    for future in done:
        response["ip"] = future.result()

    print(response)


print("Using a {} timeout".format(TIMEOUT))
ioloop = asyncio.get_event_loop()
ioloop.run_until_complete(asynchronous(TIMEOUT))
ioloop.close()
