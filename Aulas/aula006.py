# tipos primitivos e saída de dados
from builtins import input, int, print

name = input('Digite seu nome: ')
n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))
s = n1 + n2;

print("A soma de {0} com {1} é igual a {2}".format(n1, n2, s))

print(name, (name.isalpha()));
print(name, (name.islower()));
print(name, (name.isprintable()));
print(name, (name.istitle()));
print(name, (name.isdecimal()));
