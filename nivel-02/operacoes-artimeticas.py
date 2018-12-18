# coding: utf-8

#
# função que retorna soma
#

def soma(numero, parcela):
	return numero + parcela

#
# funçaõ que retorna subtração
#

def sub(numero, subtraendo):
	return numero - subtraendo

#
# função que retorna multiplicação
#

def mult(numero, multiplicador):
	return numero * multiplicador

#
# função que retorna divisão
#

def div(numero, divisor):
	return numero / divisor

#
# testes
#

assert 12 == soma(10, 2)
assert 8 == sub(10, 2)
assert 20 == mult(10, 2)
assert 5 == div(10, 2)