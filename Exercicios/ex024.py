"""
Crie um programa que leia o nome de uma cid e
diga se ela começa ou não com o nome “SANTA”.
"""

cid = str(input("Digite a cid que vc nasceu: ")).strip()
print(cid[:5].upper() == "SANTA")
print("Voce nasceu em: {}".format(cid.title()))
