# coding: utf-8

#
# retorna se o valor é par ou ímpar
#

def par_impar(valor):
    if valor % 2 == 0:
        return 'par'
    else:
        return 'impar'

#
# testes
#

assert 'par' == par_impar(2)
assert 'impar' == par_impar(3)