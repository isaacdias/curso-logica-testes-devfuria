
#
# listas
#

lista = [10, 20, 20, 50, 26]
lista2 = [10, 20, 30, 40, 50]

#
# remove os duplicados
#

def removerDuplicados(lista):
    return set(lista)

#
# retorna se há duplicados
#

def ahDuplicados(lista):
    if len(lista) != len(removerDuplicados(lista)):
        return True
    else:
        return False

#
# testes
#

assert True == ahDuplicados(lista)
assert False == ahDuplicados(lista2)