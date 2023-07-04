"""
Crie um programa que mostre na tela todos os
números pares que estão no intervalo entre 1 e 50.

"""
print("Numeros pares que estão entre 1 e 50")
for i in range(2, 51, 2):
    print("{}: Minha versão em coluna".format(i))
print("Acabou!!!")

# Versão do professor

for n in range(2, 51, 2):
    print(n, end=' ')
print("Acabou!!! Versão do Professor em linha")
