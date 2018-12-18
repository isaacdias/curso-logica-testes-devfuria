# coding: utf-8

#
# retorna se o valor é positivo ou negativo
#

def posit_negat(numero):
    if numero >= 0:
        return 'positivo'
    else:
        return 'negativo'

#
# testes
#

assert 'negativo' == posit_negat(-25)
assert 'positivo' == posit_negat(21)