# Fibonnacci
from datetime import datetime
from functools import lru_cache
# https://docs.python.org/3/library/functools.html#functools.lru_cache


def fib_sem_cache(n):
    """Forma mais convencional de fazer a sequencia de fibonnacci
    de forma recursiva, mas muito ineficiente."""
    if n < 2:
        return n
    return fib_sem_cache(n-1)+fib_sem_cache(n-2)


@lru_cache(maxsize=None)
def fib_com_cache(n):
    """A forma recursiva vista anteriormente, mas usando um lru_cache
    da functools, aumentando exponencialmente a performance."""
    if n < 2:
        return n
    return fib_com_cache(n-1)+fib_com_cache(n-2)


def fib_melhor(n):
    """Forma mais correta e elegante. Não precisa de recursividade"""
    if n == 0:
        return 0
    last = 0
    nex = 1
    for _ in range(1, n):
        last, nex = nex, last + nex
    return nex


def perform(func, arg):
    start = datetime.now()
    resp = func(arg)
    dt = datetime.now() - start
    return resp, dt.total_seconds()


if __name__ == "__main__":
    n = 35
    print("Fibonnacci: n =", n)
    print("Sem cache:\t", perform(fib_sem_cache, n))
    print("Com cache:\t", perform(fib_com_cache, n))
    print("Sem recursão:\t", perform(fib_melhor, n))
    # TODO: fazer n -> range(0, 40) e plotar um gráfico
    # TODO descobrir o Big(O) de cada caso
