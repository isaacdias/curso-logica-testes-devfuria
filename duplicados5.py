
#
# listas
#

lista = [10, 20, 20, 50, 26]
lista2 = [10, 20, 30, 40, 50]

#
# retorna se há duplicados
#

def ahDuplicados(lista):
    return len(lista) != len(set(lista))

#
# testes
#

assert True == ahDuplicados(lista)
assert False == ahDuplicados(lista2)