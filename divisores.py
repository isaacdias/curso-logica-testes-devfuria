#coding: utf-8

def divisor(num):
    cont = 1
    divisores = []
    while cont <= num:
        if num % cont == 0:
            divisores.append(cont)
        cont += 1
    return divisores


assert [1, 2, 5, 10] == divisor(10)