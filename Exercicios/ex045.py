"""
Crie um programa que faça o computador jogar Jokenpô com você.
"""
from random import randint

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
print('-=' * 10)
print("Computador jogou {}.".format(itens[computador]))
print("Jogador jogou {}.".format(itens[jogador]))
print('-=' * 10)

if computador == 0:  # Pedra

elif computador == 1:  # Papel

elif computador == 2:  # Tesoura
