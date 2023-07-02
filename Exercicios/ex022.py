"""
Crie um programa que leia o nome completo de uma pessoa e mostre:
– O nome com todas as letras maiúsculas e minúsculas.
– Quantas letras ao todo (sem considerar espaços).
– Quantas letras tem o primeiro nome.
"""

nome = str(input("Digite o nome completo: ")).strip()
print("Analisando o seu nome...")

print("Seu nome em maiúsculo é: {}. ".format(nome.upper()))
print("Seu nome em minúsculo é: {}. ".format(nome.lower()))
print("Resultado {}" .format(nome.title()))
print("Seu nome ao todo tem: {} letras ".format(len(nome) - nome.count(' ')))

print("Seu primeiro nome tem {} letras.".format(nome.find(' ')))
separa = nome.split()
print(separa)
print('Seu primeiro nome é {}  e ele tem {} letras'.format(separa[0], len(separa[0])))
