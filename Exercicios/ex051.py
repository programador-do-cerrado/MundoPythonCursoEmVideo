"""
Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
No final, mostre os 10 primeiros termos dessa progressão.

"""
a = float(input("Digite o primeiro termo da P.A.: "))
r = float(input("Digite o valor da razão dessa P.A: (utilize . para separar as casas decimais)"))

print("O primeiro termo dessa P.A. é {} e a razão é {}".format(a, r))

for c in range(0, 11):
    a = a + r
    print(a)
