# coding: utf-8

#
# função que retorna o antecessor de um número
#

def antecessor(numero):
	return numero - 1

#
# função que retorna o sucessor de um número
#

def sucessor(numero):
	return numero + 1

#
# testes
#

assert 9 == antecessor(10)

assert 11 == sucessor(10)