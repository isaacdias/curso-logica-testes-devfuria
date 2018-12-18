# coding: utf-8

#
# equação de 2 grau
#

import math

#
# retorna o valor de delta
#

def delta(a, b, c,):
    return ((b**2) - 4) * a * c

#
# retorna o valor da raiz1
#

def raiz1(a, b, c):
    return (- b + math.sqrt(delta(a, b, c))) / 2 * a

#
# retorna o valor da raiz2
#

def raiz2(a, b, c):
    return (-b - math.sqrt(delta(a, b, c))) / 2 * a

#
# testes
#

assert 64 == delta(1, 0 , -16)
assert 4 == raiz1(1, 0, -16)
assert -4 == raiz2(1, 0, -16)

