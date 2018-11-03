# coding utf-8

palavra1 = 'python'
palavra2 = 'python3'
palavra3 = 'ython'

#
# retorna se as strings são iguais
#

def compararStrings(string1, string2):
    if len(string1) == len(string2):
        i = 0
        while i < len(string1):
            if string1[i] == string2[i]:
                igual = True
            else:
                igual = False
                break
            i += 1
        return igual
    else:
        return False

#
# teste
#

assert True == compararStrings(palavra1, palavra1)
assert not True == compararStrings(palavra1, palavra2)
assert not True == compararStrings(palavra1, palavra3)