"""
Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
"""

numero = int(input("Digite um numero inteiro: "))
result = numero % 2

if (result == 0):
    print("O número {} é par".format(numero))
else:
    print("O numero {} é impar".format(numero))
