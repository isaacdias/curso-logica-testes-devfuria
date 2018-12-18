# coding: utf-8

#
# função que retorna o dobro de um numero
#

def dobro(num):
	return 2 * num

#
# teste
#

assert 12 == dobro(6)

#
# saída
#

print(dobro(int(input('Informe um numero: '))))