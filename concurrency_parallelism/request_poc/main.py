from datetime import datetime
from multiprocessing.dummy import Pool
import asyncio
import requests


# INPUTS:
# 32 workers
# 2000 tasks
# Dt ~ .5secs/task
_START = datetime.utcnow()
_QUEUE = range(2*10**3)
_POOL_SIZE = 2**6


def _task(n):
    # task: request to local app where sleep .5 secs
    r = requests.get("http://127.0.0.1:5001/hello")
    stamp = (datetime.utcnow() - _START).total_seconds()
    print(f"{n}\t{r.json()}\t%.2f" % stamp)


async def _task_async():
    asyncio.
    pass


def sync():
    for ii in _QUEUE:
        _task(ii)


def pool_map():
    pool = Pool(_POOL_SIZE)
    pool.map(_task, _QUEUE)
    pool.close()
    pool.join()


def asynci_simple():
    asyncio.run(_task_async())
    pass


if __name__ == "__main__":
    # sync()  # ~ 1020 secs
    # pool_map()  # ~ 17.1 secs
    asynci_simple()
