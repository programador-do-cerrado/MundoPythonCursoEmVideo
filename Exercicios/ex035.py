"""
Desenvolva um programa que leia o comprimento de três retas
em seguida diga ao usuário se elas podem ou não formar um triângulo.
"""

r1 = float(input("Reta 1: "))
r2 = float(input("Reta 2: "))
r3 = float(input("Reta 3: "))

if (r1 < r2 + r3) and (r2 < r3 + r1) and (r3 < r2 + r1 ):
    print("É POSSÍVEL formar um triângulo")
else:
    print("É IMPOSSIVEL formar um triângulo")
