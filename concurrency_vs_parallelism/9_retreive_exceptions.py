from collections import namedtuple
import time
import asyncio
import aiohttp

Service = namedtuple('Service', ('name', 'url', 'ip_attr'))

SERVICES = [{'name': 'ipify', 'url': 'https://api.ipify.org?format=json', 'ip_attr': 'ip'},
            {'name': 'ip-api', 'url': 'http://ip-api.com/json', 'ip_attr': 'query'},
            {'name': 'broken', 'url': 'http://some-random-broken-url.com/json', 'ip_attr': 'ip'}  # This url won't work
            ]


async def find_my_ip(service):
    """ Get current IP address by hitting 3rd party APIs"""
    start = time.time()
    print('Fetching IP from {}'.format(service['name']))

    try:
        response = await aiohttp.request('GET', service['url'])
    except:
        print('{} is unresponsive'.format(service['name']))
    else:
        json_response = await response.json()
        ip = json_response[service['ip_attr']]

        response.close()
        print('{} finished with result: {}, took: {:.2f} seconds'.format(
            service['name'], ip, time.time() - start))


async def asynchronous():
    """ Initialize asynchronous task"""
    futures = [find_my_ip(service) for service in SERVICES]
    await asyncio.wait(futures)  # intentionally ignore results


ioloop = asyncio.get_event_loop()
ioloop.run_until_complete(asynchronous())
ioloop.close()
