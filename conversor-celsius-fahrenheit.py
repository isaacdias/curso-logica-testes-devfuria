# coding: utf-8

#
# função que coverte Fahrenheit para Celsius
#

def toCelsius(fahrenheit):
	return (fahrenheit - 32) * 5 / 9

#
# função que converte de Celsius para Fahrenheit
#

def toFahrenheit(celsius):
	return (celsius * 9 / 5) + 32 

#
# testes
#

assert 100 == toCelsius(212)
assert 212 == toFahrenheit(100)