"""
Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
No final, mostre os 10 primeiros termos dessa progressão.

"""
a = float(input("Primeiro Termo: "))
r = float(input("Razão: (utilize . para separar as casas decimais)"))

print("O primeiro termo dessa P.A. é {:.2f} e a razão é {:.2f}".format(a, r))

for c in range(0, 11):
    a = a + r
    print('{:.2f} '.format(a), end="-> ")
print("ACABOU ")
