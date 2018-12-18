# coding: utf-8

#
# funcao que retorna divisores
#

def divisor(num):
    divisores = []

    for i in range(1, num + 1):
        if num % i == 0:
            divisores.append(i)
    return divisores

#
# testes
#

assert [1, 2, 5, 10] == divisor(10)