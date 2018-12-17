#coding: utf-8

#
# funçao que retorna o fatorial de um numero
#

def fatorial(n):
    if n <= 1:
        return 1
    else:
        return n * fatorial(n-1)

#
# teste
#

assert 120 == fatorial(5)