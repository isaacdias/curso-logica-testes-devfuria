#coding: utf-8

#
# criada uma classe
#

class Triangulo(object):

#
# criado um metodo construtor
#

    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

#
# criado o metodo que retorna se é triangulo
#

    def valida_forma(self):
        if self.lado1 < (self.lado2 + self.lado3):
            if self.lado2 < (self.lado1 + self.lado3):
                if self.lado3 < (self.lado2 + self.lado3):
                    return True

        return False

#
# instancia da classe 'Triangulo' já com os parametros
#
triangulo = Triangulo(3, 4, 5)

#
# teste
#

assert triangulo.valida_forma()

#
# instancia da classe 'Triangulo' á com parametros
#

triangulo = Triangulo(1 , 3, 0)

#
# teste
#

assert not triangulo.valida_forma()