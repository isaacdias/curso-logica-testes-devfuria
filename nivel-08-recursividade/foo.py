# coding: utf-8

#
# Datas
#

from datetime import datetime
now = datetime.now()

print(now)
print(now.year)
print(now.month)
print(now.day)

#
# Para imprimir a data no formato brasileiro
#

print('%s/%s/%s' %(now.day, now.month, now.year))

#
# Imprimindo as horas
#

print('%s:%s:%s' %(now.hour, now.minute, now.second))

