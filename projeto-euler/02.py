# coding: utf-8

#
# funcao que retorna a soma dod termos pares de fibonacci
# ate 4 milhoes
#

def soma_fibonacci_pares(numero, limite):
    pares = []
    a,b = 0,1
    for i in range(numero):
        a,b = b,a+b
        if b % 2 == 0 and b < limite:
            pares.append(b)
    return sum(pares)

#
# teste
#

assert 44 == soma_fibonacci_pares(10, 50)

#
# resultado
#

print(soma_fibonacci_pares(100, 4000000))
