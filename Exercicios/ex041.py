"""

A Confederação Nacional de Natação precisa de um programa que:
leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
    * Até 9 anos: MIRIM
    * Até 14 anos: INFANTIL
    * Até 19 anos: JÚNIOR
    * Até 25 anos: SÊNIOR
    * Acima de 25 anos: MASTER
"""
from datetime import date

nasc = int(input("Digite o ano de nascimento do atleta: AAAA "))
atual = date.today().year
idade = atual - nasc

print("Estamos em {} e o atleta tem {} anos".format(atual, idade))

if idade <= 9:
    print("Categoria MIRIM")
elif idade > 9 and idade <= 14:
    print("Categoria INFANTIL")
elif idade > 14 and idade <= 19:
    print("Categoria JÚNIOR")
elif idade > 19 and idade <= 35:
    print("Categoria SÊNIOR")
else:
    print("Categoria MASTER")
