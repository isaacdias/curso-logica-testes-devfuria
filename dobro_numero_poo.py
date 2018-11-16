#coding: utf-8

#
# classe Calc com função que retorna o dobro de um numero
#

class Calc(object):

 def dobro(self, num):
    return num * 2

#
# instancia da classe
#

calc = Calc()

#
# teste
#

assert 10 == calc.dobro(5)