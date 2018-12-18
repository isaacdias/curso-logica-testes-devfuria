# coding: utf-8

#
# funao que retorna os divisores
#

def divisor(num):
    cont = 1
    divisores = []
    while cont <= num:
        if num % cont == 0:
            divisores.append(cont)
        cont += 1
    return divisores

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