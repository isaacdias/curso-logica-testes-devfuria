# coding: utf-8

def divisor(num):
    divisores = []

    for i in range(1, num + 1):
        if num % i == 0:
            divisores.append(i)
    return divisores


assert [1, 2, 5, 10] == divisor(10)