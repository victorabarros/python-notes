from datetime import datetime
from functools import partial
from multiprocessing.dummy import Pool
from time import sleep


def sleep_and_print(start, n):
    print(n, "\t", datetime.utcnow().isoformat()[:-4])
    sleep(1)
    # print(n, (datetime.utcnow() - start).total_seconds())


def apply_async():
    pool_request = Pool(4)
    start = datetime.utcnow()
    print(start)

    for ii in [1, 2, 3, 4, 5]:
        pool_request.apply_async(sleep_and_print, (start, ii))

    pool_request.close()
    pool_request.join()


def pool_map():
    pool = Pool(2**6)
    start2 = datetime.utcnow()
    print(start2)

    pool.map(partial(sleep_and_print, start2), range(30))

    pool.close()
    pool.join()


def sync():
    start3 = datetime.utcnow()
    print(start3)

    for ii in range(30):
        sleep_and_print(start3, ii)


if __name__ == "__main__":
    # apply_async()
    pool_map()
    # sync()
