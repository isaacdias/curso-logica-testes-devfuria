# coding: utf-8

#
# função que retorna reajuste de salário
#

def reajuste_salario(salario, reajuste):
	return salario * reajuste

#
# teste
#

assert 150 == reajuste_salario(1000, 0.15)
	
