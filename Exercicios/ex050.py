"""
Desenvolva um programa que leia seis números inteiros
e mostre a soma apenas daqueles que forem pares.
Se o valor digitado for ímpar, desconsidere-o.
"""

s = 0
for x in range(1, 7):
    numDigitado = int(input("Digite o {}º valor: ".format(x)))
    if numDigitado % 2 == 0:
        s = s + numDigitado
print("O somatorio de todos os valores pares digitados é {}".format(s))

# --------------------------
sImpar = 0
for y in range(1, 7):
    numDigitadoFim = int(input("Digite o {}º valor: ".format(y)))
    if numDigitadoFim % 2 != 0:
        sImpar = s + numDigitadoFim
print("O somatorio de todos os valores impares digitados é {}".format(sImpar))
