
#
# listas
#

lista = [10, 20, 20, 50, 26]
lista2 = [10, 20, 30, 40, 50]

#
# retorna se ha duplicados na lista
#

def ahDuplicados(lista):
    lis = []
    for i in lista:
        if i not in lis:
            lis.append(i)

    if len(lis) != len(lista):
        return True
    else:
        return False

#
# testes
#

assert True == ahDuplicados(lista)
assert False == ahDuplicados(lista2)