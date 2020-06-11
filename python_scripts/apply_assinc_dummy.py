from multiprocessing.dummy import Pool
from time import sleep


def print_and_sleep(n):
    sleep(n)
    print(n)


pool_request = Pool(8)

if __name__ == "__main__":
    data = [1, 2, 3]
    pool_request.apply_async(print_and_sleep, data)
