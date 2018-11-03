# coding: utf-8

s = 'python'
vogais = 'aeiou'

#
# retorna quantidade de vogais
#

def quant_vogais(s):
    cont = 0
    for i in s:
        if i in vogais:
            cont += 1
    return cont

#
# testes
#

assert 1 == quant_vogais(s)


