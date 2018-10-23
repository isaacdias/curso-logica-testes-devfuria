# coding: utf-8

#
# função que retrona o custo final de um carro
#

def custo_final(custo_fabrica, distribuidor, imposto):
    return custo_fabrica + (custo_fabrica * distribuidor) + (custo_fabrica * imposto)

#
# teste
#

assert 17300 == custo_final(10000, 0.28, 0.45)