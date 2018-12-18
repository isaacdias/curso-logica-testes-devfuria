# coding: utf-8

#
# lista
#

lista = [10, 50, 23, -100]

#
# retorna o indice com o maior valor
#

def maior_indice(lista):
    iMaior = 0
    i = 0
    while i < len(lista):
        if lista[i] > lista[iMaior]:
            iMaior = i
        i += 1
    return iMaior

#
# retorna o indice com o menor valor
#

def menor_indice(lista):
    iMenor = 0
    i = 0
    while i < len(lista):
        if lista[i] < lista[iMenor]:
            iMenor = i
        i += 1
    return iMenor

#
# testes
#

assert 1 == maior_indice(lista)
assert 3 == menor_indice(lista)