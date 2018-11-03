# coding: utf-8

palavra = 'animal'

#
# retorna uma string ivertida
#

def inverterString(string):
    lista = list(string)
    i = 0
    nova_palavra = []
    while i < len(lista):
        nova_palavra.append(lista[i])
        i += 1
    nova_palavra.reverse()
    return ''.join(nova_palavra)

#
# teste
#

assert 'lamina' == inverterString(palavra)