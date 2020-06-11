from typing import Dict


# Utilizing base cases
def fib2(n: int) -> int:
    if n < 2:  # base case
        return n
    return fib2(n - 2) + fib2(n - 1)  # recursive case


# Memoization to the rescue
memo: Dict[int, int] = {0: 0, 1: 1}  # our base cases


def fib3(n: int) -> int:
    if n not in memo:
        memo[n] = fib3(n - 1) + fib3(n - 2)  # memoization
    return memo[n]


def fib5(n: int) -> int:
    if n == 0:
        return n  # special case
    last: int = 0  # initially set to fib(0)
    _next: int = 1  # initially set to fib(1)
    for _ in range(1, n):
        last, _next = _next, last + _next
    return _next


if __name__ == "__main__":
    from datetime import datetime
    nn = [2*(10*_nn) for _nn in range(25)]
    funcs = [
        # fib2,
        fib3,
        fib5
    ]

    for func in funcs:
        start = datetime.utcnow()

        result = list()
        for ii in nn:
            fib_str = str(func(ii))
            result.append(fib_str)
            # print(ii, fib_str)

        dt = datetime.utcnow() - start
        print(dt)
