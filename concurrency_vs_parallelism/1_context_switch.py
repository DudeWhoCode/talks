import asyncio


# Co-routine 1
async def task1():
    print('Started task1')
    # await gives the control flow back to the event loop
    await asyncio.sleep(10)
    print('Context switch to task1 again')


# Co-routine 2
async def task2():
    print('Started task2 after context switch')
    await asyncio.sleep(10)
    print('Context switch back to task2')

# Get an eventloop object from asyncio
ioloop = asyncio.get_event_loop()

# create_task wraps the coroutine object in a future and returns task object
future1 = ioloop.create_task(task1())
future2 = ioloop.create_task(task2())

# Arrange your tasks into a queue(list)
tasks = [future1, future2]

# combine them into one that waits for both of the coroutines to complete
wait_tasks = asyncio.wait(tasks)

# feed the tasks into the event loop, run until the future is done
ioloop.run_until_complete(wait_tasks)

# close the eventloop
ioloop.close()
