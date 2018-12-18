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
    for index, item in enumerate(lista):
        if lista[index] > lista[iMaior]:
            iMaior = index
    return iMaior

#
# retorna o indice com o menor valor
#

def menor_indice(lista):
    iMenor = 0
    for index, item in enumerate(lista):
        if lista[index] < lista[iMenor]:
            iMenor = index
    return iMenor

#
# testes
#

assert 1 == maior_indice(lista)
assert 3 == menor_indice(lista)
