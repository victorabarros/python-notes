from multiprocessing.pool import ThreadPool
from time import sleep, time

def square(a):
    print('start', a)
    sleep(a)
    print('end', a)
    return a * a

def encaps(a):
    square(**a)

def main1():
    p = ThreadPool(processes=2)
    queue_a = [
        {
            'a': 1
        },{
            'a': 2
        },{
            'a': 3
        },{
            'a': 4
        }]
    start = time()
    p.map(partial(square, queue_a))
    print(time() - start)

def square2(a, b):
    print('start', a, b)
    sleep(a)
    print('end', a, b)
    return a * a

def main3():
    p = ThreadPool(processes=2)
    queue_a = [[1,1],[2,2],[3,3],[4,4]]
    
    example = [
        {"a": 1, "b": 1},
        {"a": 2, "b": 2},
        {"a": 3, "b": 3},
        {"a": 4, "b": 4}
    ]
    
    queue_a = [list(x.values()) for x in example.values()]
    
    start = time()
    p.starmap(square, queue_a)
    print(time() - start)

def main2():
    p = ThreadPool(2)
    queue = list(range(4))
    start = time()
    p.apply_async(square, args=(4,))
    print(time() - start)

if __name__ == "__main__":
    main2()
