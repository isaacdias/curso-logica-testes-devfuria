#coding: utf-8


#
# fun�ao que retorna a soma de numeros 
#

def add(n):
    if n != 0:
        return n + add(n-1)
    else:
        return 0

#
# chamada da fun�ao
#

add(6)

#
# teste
#

assert 21 == add(6)