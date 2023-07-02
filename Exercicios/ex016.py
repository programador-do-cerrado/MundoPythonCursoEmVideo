"""
Exercício Python 16: Crie um programa que leia um número Real
qualquer pelo teclado e mostre na tela a sua porção Inteira.
"""
"""import math
numero = float(input("Digite um número real (mas utilize ponto, e não virgula): "))
print("O valor digitado foi {} e a sua porção inteira é {}".format(numero, math.trunc(numero)))
"""
numero = float(input("Digite um número real (mas utilize ponto, e não virgula): "))
print("O valor digitado foi {} e a sua porção inteira é {:.0f}".format(numero, numero))
