#coding: utf-8

#
# retorna os divisores
#

def divisor(num):
    cont = 1
    divisores = []
    while cont <= num:
        if num % cont == 0:
            divisores.append(cont)
        cont += 1
    return divisores