#coding: utf-8

#
# classe que retorna antecessor e sucessor de un numero
#

class Calc(object):

    def antecessor(self):
        return self.num - 1

    def sucessor(self):
        return self.num + 1

#
# istancia da classe
#
calc = Calc()

#
# testes
#

calc.num = 4
assert 3 == calc.antecessor()

calc.num = 4
assert 5 == calc.sucessor()