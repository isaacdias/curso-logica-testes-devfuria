# coding: utf-8

#
# ciando uma lista
#

lista = []
for i in range(1 , 5 + 1):
    lista.append(i)

#
# retrna a soma da lista
#

def soma_vetor(lista):
    soma = 0
    for i in lista:
        soma += i
    return soma

#
# testes
#

assert 15 == soma_vetor(lista)
        
    
