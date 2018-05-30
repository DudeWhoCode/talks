import random
from time import sleep
import asyncio


def task_sync(pid):
    sleep(random.randint(0, 5) * 0.1)
    print('Task %s done' % pid)


async def task_async(pid):
    await asyncio.sleep(random.randint(0, 5) * 0.1)
    print('Task %s done' % pid)


def synchronous():
    """ Initialize synchronous task"""
    for i in range(1, 10):
        task_sync(i)


async def asynchronous():
    """ Initialize asynchronous task"""
    tasks = []
    # We are queueing up the tasks in the same order as in synchronous() function
    for i in range(1, 10):
        # ensure future is a method to create Task from coroutine
        task = asyncio.ensure_future(task_async(i))
        tasks.append(task)

    await asyncio.wait(tasks)

# Kick off synchronous task
print('Synchronous:')
synchronous()

# Kick off asynchronous task
ioloop = asyncio.get_event_loop()

print('Asynchronous:')
ioloop.run_until_complete(asynchronous())
ioloop.close()
