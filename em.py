import functools
import timeit

def fib_1(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib_1(n-1) + fib_1(n-2)

@functools.lru_cache()
def fib_2(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib_2(n-1) + fib_2(n-2)

a = int(input())

print( timeit.timeit("fib_1(a)", setup="from __main__ import fib_1, a", number=10000) )
print( timeit.timeit("fib_2(a)", setup="from __main__ import fib_2, a", number=10000) )
