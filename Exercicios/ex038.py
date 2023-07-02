"""
Escreva um programa que leia dois números inteiros e compare-os.
mostrando na tela uma mensagem:
    – O primeiro valor é maior
    – O segundo valor é maior
    – Não existe valor maior, os dois são iguais
"""
print("Digite apens números inteiros: ")
num1 = int(input("Digite o valor 1: "))
num2 = int(input("Digite o valor 2: "))

if num1 > num2:
    print("O primeiro valor: {} é maior que o segundo valor: {}".format(num1, num2))
elif num2 > num1:
    print("O segundo valor: {} é maior que o primeiro valor: {}".format(num2, num1))
else:
    print("Os números digitados são iguais")
