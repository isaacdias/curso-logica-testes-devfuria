# coding: utf-8

#
# listas
#

lista1 = [1, 2, 3, 4, 5, 6]
lista2 = []

#
# funcao que copia itens da lista1 para outra
#

def copiar_lista(lista1):
    nova_lista = []
    for i in lista1:
        nova_lista.append(i)
    return nova_lista


lista2 = copiar_lista(lista1)

#
# teste
#

assert lista1 == lista2
