import asyncio


# Co-routine 1
async def task1():
    print('Started task1')
    await asyncio.sleep(0)
    print('Context switch to task1 again')


# Co-routine 2
async def task2():
    print('Started task2 after context switch')
    # await gives the control flow back to the event loop
    await asyncio.sleep(0)
    print('Context switch back to task2')

# using create_task as implementing our own event loop type.
ioloop = asyncio.get_event_loop()
tasks = [ioloop.create_task(task1()), ioloop.create_task(task2())]
wait_tasks = asyncio.wait(tasks)
# feed the tasks into the event loop
ioloop.run_until_complete(wait_tasks)
ioloop.close()
