#coding: utf-8

#
# funçao que retorna fibonacci
#

def fib(n):
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)

#
# teste
#

assert 1 == fib(1)
assert 1 == fib(2)
assert 2 == fib(3)
assert 3 == fib(4)
assert 5 == fib(5)