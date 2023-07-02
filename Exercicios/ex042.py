"""
Refaça o DESAFIO 35 dos triângulos,
acrescentando o recurso de mostrar que
tipo de triângulo será formado:
    * EQUILÁTERO: todos os lados iguais
    * ISÓSCELES: dois lados iguais, um diferente
    * ESCALENO: todos os lados diferentes
"""
r1 = float(input("Reta 1: "))
r2 = float(input("Reta 2: "))
r3 = float(input("Reta 3: "))

if (r1 < r2 + r3) and (r2 < r3 + r1) and (r3 < r2 + r1):
    print("É POSSÍVEL formar um triângulo")
    if r1 == r2 and r1 == r3:
        " r1 == r2 == r3 "
        print("Formou um triângulo EQUILATERO")
    elif r1 != r2 != r3 != r1:
        print("Formou um triângulo ESCALENO")
    else:
        print("Triângulo ISÓSCELES")
else:
    print("É IMPOSSIVEL formar um triângulo")
