#!/usr/bin/python3

import lib

def naive(n: int) -> int:
        
    if (n == 0 or n == 1):
        return n
    else:
        return naive(n - 1) + naive(n - 2)


@lib.exeTime
def fib(n: int) -> int:
    return naive(n)


if __name__ == "__main__":

    a = fib(50)
    print("a =", a)
