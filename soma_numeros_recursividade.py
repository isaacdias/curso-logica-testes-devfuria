#coding: utf-8


#
# funçao que retorna a soma de numeros 
#

def add(n):
    if n != 0:
        return n + add(n-1)
    else:
        return 0

#
# chamada da funçao
#

add(6)

#
# teste
#

assert 21 == add(6)