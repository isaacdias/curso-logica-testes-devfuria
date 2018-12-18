# coding: utf-8

#
# importando funcao
#

from meu_modulo import divisor

#
# funao que retona se o numero e primo
#

def primo(num):
    div = divisor(num)

    if len(div) == 2:
        return True
    else:
        return False

#
# testes
#

assert primo(2)
assert primo(3)

assert not primo(1)
assert not primo(10)