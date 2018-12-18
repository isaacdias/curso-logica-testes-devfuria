#coding: utf-8

#
# criada uma classe
#

class Juros():
    pass

#
# instancia da classe 'Juros'
#

juros = Juros()

#
# deinido uma funcao para o metodo atraves do lambda
#

juros.simples = lambda obj: obj.capital * obj.taxa * obj.periodo

#
# teste
#

juros.capital = 16000
juros.taxa = 0.04
juros.periodo = 4
assert 2560 == juros.simples(juros)