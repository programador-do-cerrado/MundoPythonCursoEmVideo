"""
Desenvolva um programa que leia as duas notas de um aluno
e em seguida cacule a média
"""

nota1 = float(input("Digite a nota do primeiro bimestre: "))
nota2 = float(input("Digite a nota do segundo bimestre: "))
media = (nota1 + nota2) / 2
print("A nota1 vale {}, a nota 2 vale {} e a media final vale: {} ".format(nota1, nota2, media))
