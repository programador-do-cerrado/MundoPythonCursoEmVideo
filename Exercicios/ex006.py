"""
crie um algoritmo que leia um numero e mostre
seu dobro, seu triplo e sua raiz quadrada
"""
from builtins import input

n1 = int(input("Digite umnúmero inteiro: "))

dob = n1 * 2
trip = n1 * 3
sqrt = n1 ** (1 / 2)
print('O dobro vale: {}, o triplo vale: {}, e a raiz quadrada vale:{:.3f}'.format(dob, trip, sqrt))
