from multiprocessing import Process
import os


def info(title):
    print(title, '\tmodule name:', __name__)
    print(title, '\tparent process:', os.getppid())
    print(title, '\tprocess id:', os.getpid())


def f(name):
    info('function f')
    print('hello', name)


if __name__ == '__main__':
    p = Process(target=f, args=('bob',))
    p.start()
    p.join()
    info('main line')
