#coding: utf-8

#
#
#
def bubblesort(mylist):
    for i in range(len(mylist)):
        for k in range(0, len(mylist) - 1 - i):
            if mylist[k] > mylist[k+1]:
                tmp = mylist[k]
                mylist[k] = mylist[k+1]
                mylist[k+1] = tmp
    return mylist


#
# teste
#

entrada = [50, 30, 20, 40, 70, 10, 0, 60]
print('entrada:' + str(entrada) + '\n')

saida = bubblesort(entrada)
print('\nsaida: ' + str(saida) + '\n')