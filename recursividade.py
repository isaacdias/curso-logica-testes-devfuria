#coding: utf-8

#
# funçao que faz contagem regressiva
#

def contagemRegressiva(n):
    if n == 0:
        print('Decolar!')
    else:
        print(n)
        contagemRegressiva(n-1)

#
# chamada da funçao
#

contagemRegressiva(5)
