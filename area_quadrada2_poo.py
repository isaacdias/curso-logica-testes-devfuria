#coding: utf-8

#
# classe Area com metodos que retornam uma determinada area
#

class Area(object):
    
    def areaQuadrada(self):
        return self.comprimento * self.largura

    def areaCubica(self):
        return self.altura * self.comprimento * self.largura

#
# instancia da classe Area
#

area = Area()

#
# testes
#

area.comprimento = 3
area.largura = 3
assert 9 == area.areaQuadrada()

area.altura = 2
area.comprimento = 3
area.largura = 3
assert 18 == area.areaCubica()
