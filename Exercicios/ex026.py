"""
Faça um programa que leia uma frase pelo teclado
e mostre quantas vezes aparece a letra “A”,
em que posição ela aparece a primeira vez
e em que posição ela aparece a última vez.
"""

frase = str(input("Digite uma frase qualquer: ")).strip().upper()
print("Voce digitou: {}".format(frase))
print("A letra 'A' aparece {} vezes".format(frase.count("A")))
print("O primeiro A aparece na {}ª posição.".format(frase.find('A') + 1))
print("O último A aparece na {}ª posição.".format(frase.rfind('A') + 1))
