"""
Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício,
indo de 10 até 0, com uma pausa de 1 segundo entre eles.
"""
from time import sleep

for f in range(10, 0, -1):
    print("Contagem regressiva: {} ".format(f))
    sleep(0.3)
print("Feliz ano novo")