#coding: utf-8

#
#
#
def bubblesort(mylist):
    for i in range(len(mylist)):
        print('[' + str(i) + '] ', end='')

        for k in range(0, len(mylist)):
            print(str(k) + ', ', end='')

        print()
    
    return mylist


#
# teste
#

entrada = [50, 30, 20, 40, 70, 10, 0, 60]
print('entrada:' + str(entrada) + '\n')

saida = bubblesort(entrada)
print('\nsaida: ' + str(saida) + '\n')