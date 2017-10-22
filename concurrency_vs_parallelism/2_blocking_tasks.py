import time
import asyncio

start = time.time()


def tic():
    return 'at %1.1f seconds' % (time.time() - start)


async def task1():
    print('task1 started work: {}'.format(tic()))
    # Blocking task for 2 seconds, But we will handover control flow back to eventloop
    await asyncio.sleep(2)
    print('task1 ended work: {}'.format(tic()))


async def task2():
    print('task2 started work: {}'.format(tic()))
    # Blocking task for 2 seconds, But we will handover control flow back to eventloop
    await asyncio.sleep(2)
    print('task2 Ended work: {}'.format(tic()))


async def task3():
    print("Task 3 kicks off when task1, task2 co-routines are blocked, {}".format(tic()))
    await asyncio.sleep(1)
    print("Task 3 is Done!")


ioloop = asyncio.get_event_loop()
tasks = [
    ioloop.create_task(task1()),
    ioloop.create_task(task2()),
    ioloop.create_task(task3())
]
wait_tasks = asyncio.wait(tasks)
ioloop.run_until_complete(wait_tasks)
ioloop.close()
