"""
Crie um programa que faça o computador jogar Jokenpô com você.
"""
from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)

print(
    """
    Suas opções:
    [ 0 ] PEDRA
    [ 1 ] PAPEL
    [ 2 ] TESOURA
  """
)
jogador = int(input("Digite sua jogada "))

print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO!!!")

print('-=' * 10)
print("Computador jogou {}.".format(itens[computador]))
print("Jogador jogou {}.".format(itens[jogador]))
print('-=' * 10)

if computador == 0:  # Pedra
    if jogador == 0:
        print("EMPATE")
    elif jogador == 1:
        print("Voce ganhou.")
    elif jogador == 2:
        print("Você perdeu")
    else:
        print("Opção inválida. Não tente roubar.")
elif computador == 1:  # Papel
    if jogador == 0:
        print("Voce perdeu.")
    elif jogador == 1:
        print("EMPATE")
    elif jogador == 2:
        print("Você ganhou")
    else:
        print("Opção inválida. Não tente roubar.")
elif computador == 2:  # Tesoura
    if jogador == 0:
        print("Voce ganhou.")
    elif jogador == 1:
        print("VocÊ perdeu")
    elif jogador == 2:
        print("EMPATE")
    else:
        print("Opção inválida. Não tente roubar.")
