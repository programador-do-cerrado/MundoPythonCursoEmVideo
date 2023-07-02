"""
Crie um programa que leia o nome de uma pessoa
e diga se ela tem “SILVA”
"""
nome = str(input("Digite seu nome completo: ")).strip().title()
print(nome)
print("Seu nome tem Silva? {} ".format('SILVA' in nome.upper()))
