# coding: utf_8

#
# classe vazia
#

class Juros(object):
    pass

#
# Criada uma funcao que retorna o valor do juros simples
#

def minha_funcao(obj):
    return obj.capital * obj.taxa * obj.periodo

#
# instancia da classe
#

juros = Juros()

#
# atribuicao da funçao ao metodo do objeto
#

juros.simples = minha_funcao

#
# teste
#

juros.capital = 16000
juros.taxa = 0.04
juros.periodo = 4
assert 2560 == juros.simples(juros)