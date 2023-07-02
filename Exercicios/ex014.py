"""Escreva um programa que converta uma temperatura
digitando em graus Celsius e converta
para graus Fahrenheit."""
from pip._vendor.rich.cells import cell_len

celcius = float(input("Digite a temperatura em Cº: "))
fahrenheit = (celcius * 1.8) + 32
print("{}ºC  e convertido para Fahrenheit é igual a {}ºF".format(celcius, fahrenheit))
