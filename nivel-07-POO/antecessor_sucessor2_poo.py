#coding: utf-8

#
# classe que retorna antecessor e sucessor de un numero
#

class Calc(object):

    def antecessor(num):
        return num - 1

    def sucessor(num):
        return num + 1

#
# testes
#

assert 3 == Calc.antecessor(4)
assert 5 == Calc.sucessor(4)