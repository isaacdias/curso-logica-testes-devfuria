#coding: utf-8

#
# fun�ao que retorna o fatorial de um numero
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