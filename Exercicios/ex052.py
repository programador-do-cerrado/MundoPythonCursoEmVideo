"""
 Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

"""

num = int(input("Digite um numero: "))
tot = 0
# tot é o total de divisiveis
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[34m', end=' ')
        tot += 1
    else:
        print('\033[31m', end=' ')
    print("{}".format(c), end=' ')
print("O número {} foi divisivel {} vezes".format(num, tot))
if tot == 2:
    print("O número {} não é primo".format(num))
elif tot > 2:
    print("O número {} não é primo.".format(num))
