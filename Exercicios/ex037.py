"""
 Escreva um programa em Python que leia um número inteiro qualquer
e peça para o usuário escolher qual será a base de conversão:
    * 1 para binário,
    * 2 para octal
    * 3 para hexadecimal.
"""
num = int(input("Digite um numero inteiro: "))

print("Escolha uma das bases para conversão: ")
print("[ 1 ] converter para BINÁRIO: ")
print("[ 2 ] converter para OCTAL: ")
print("[ 3 ] converter para HEXADECIMAL: ")
opcao = int(input("Sua opção: "))

print("Você digitou: {}".format(num))

if opcao == 1:
    print("{} convertido para BINARIO é igual a {}".format(num, bin(num)[2:]))
elif opcao == 2:
    print("{} convertido para OCTAL é igual a {}".format(num, oct(num)[2:]))
elif opcao == 3:
    print("{} convertido para HEXADECIMAL é igual a {}".format(num, hex(num)[2:]))
else:
    print("Opção inválida")
