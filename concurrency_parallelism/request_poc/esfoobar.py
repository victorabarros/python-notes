# https://medium.com/@esfoobar/python-asyncio-for-beginners-c181ab226598
from datetime import datetime
import asyncio

_START = datetime.utcnow()


def stopwatch():
    return "%.2f"%(datetime.utcnow() - _START).total_seconds()

async def waiter():
    task1 = asyncio.create_task(cook('Italy Pasta', 8))
    task2 = asyncio.create_task(cook('Caesar Salad', 3))
    task3 = asyncio.create_task(cook('Lamb Chops', 16))

    await task1
    await task2
    await task3


async def cook(order, time_to_prepare):
    print(f'{stopwatch()}\t{order}\t\tstarted')
    await asyncio.sleep(time_to_prepare)
    print(f'{stopwatch()}\t{order}\t\tdone')

asyncio.run(waiter())
