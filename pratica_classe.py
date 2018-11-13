#coding: utf-8

#
# criação de uma classe com um metodo que inicializa a variavel a
#

class Foo(object):
    def lish(self):
        self.a = 123
        return self.a

#
# instancia de uma classe
#

f = Foo()

#
# executa a função da classe Foo
#

f.lish()

#
# verificação da execução
#

print(f.a)

