"""
Faça um programa que leia o nome completo de uma pessoa, 
mostrando em seguida o primeiro e o último nome separadamente.
"""

nome = str(input("Digite seu nome completo: ")).strip().title()
n = nome.split()
print("Seja bem vindo {}.".format(nome.title()))
print('Seu primeiro nome é {}.'.format(n[0]))
print('Seu último sobrenome é {}.'.format(n[len(n)-1]))
