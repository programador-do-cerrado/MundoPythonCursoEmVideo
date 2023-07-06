"""
Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,
desconsiderando os espaços.
Exemplos de palíndromos:
    APOS A SOPA,
    A SACADA DA CASA,
    A TORRE DA DERROTA,
    O LOBO AMA O BOLO,
    ANOTARAM A DATA DA MARATONA.
"""

frase = str(input("Digite uma frase: ")).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''

# Até aqui, o ususario digita a frase e o algoritimo une a frase tirando os espaços

for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print(junto, inverso)
if junto == inverso:
    print("Você digitou um palíndromo")
else:
    print("O que vc digitou não é um palíndromo")

print("***" * 20)

inverso2 = junto[::-1]
if junto == inverso2:
    print("Você digitou um palíndromo")
else:
    print("O que vc digitou não é um palíndromo")
print(("Resultado do segundo exemplo"))
