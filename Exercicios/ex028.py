"""
Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5
em seguida, peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu.

"""
import random

computador = random.randint(0,5)
print("-=-" * 25)
print("eu estou pensando em um número entre 0 e 5. Você consegue advinhar qual é?")
print("-=-" * 25)
user = int(input("Digite qual número que vc acha que é: "))
print("-=-" * 25)

if (user == computador):
    print("parabéns, você acertou")
    print("-=-" * 25)
elif (user >= 0 and user <= 5 ):
    print("Você digitou o {}, porém eu pensei no {}.".format(user, computador))
    print("-=-" * 25)
else:
    print("O número {} nem está entre 0 e 5, eu pensei no {}. ".format(user, computador))
    print("-=-" * 25)
