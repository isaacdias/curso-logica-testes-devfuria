#coding: utf-8

#
# classe com meodos qe retorna a area uadrada e cubica
#

class Area(object):
    def areaQuadrada(self, comprimento, largura):
        return comprimento * largura

    def areaCubica(self, altura, comprimento, largura):
        return altura * comprimento * largura

#
# instancia de Area
#
area = Area()
area.areaQuadrada(3, 3)
area.areaCubica(3, 3, 3)

#
# testes
#

assert 9 == area.areaQuadrada(3, 3)
assert 27 == area.areaCubica(3, 3, 3)