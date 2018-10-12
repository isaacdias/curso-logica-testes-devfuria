# coding: utf-8

#
# função que calcula juros simples de um empréstimo
#
def juros(capital, taxa, meses):
	return capital * juros * meses

#
# teste
#

assert 100 == juros(1000, 0.05, 2)