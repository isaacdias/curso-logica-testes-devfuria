# coding: utf-8

#
# entrada
#
a = 999
b = 555

#
# processamento
#

temp = a
a = b
b = temp

#
# testes
#

assert a == 555
assert b == 999