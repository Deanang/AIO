#Test
print('Hello', 'What', 'Tired', 'last'å)
import sys
sys.setrecursionlimit(20000)
from time import time

def fib(x):
  if x == 1 or x == 2:
    return 1
  else:
    return fib(x-1) + fib(x-2)

start = time()
fib(30)
end = time()
print(end-start)

def memo(f):
    d = dict()
    def helper(x):
        if x not in d:
            d[x] = f(x)
        return d[x]
    return helper

fib = memo(fib)

start = time()
fib(5000)
end = time()
print(end-start)
