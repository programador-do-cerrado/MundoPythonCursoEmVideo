"""
Faça um programa que leia a largura e a altura de uma parede em metros,
calcule a sua áreae a quantidade de tinta necessária para pintá-la, sabendo que
cada litro de tinta, pinta uma área 2 m².

"""
larg = float(input("largura da parede: "))
alt = float(input("altura da parede: "))
area = alt * larg
print("Sua parede tem a dimensão de {} X {} e a sua área é de {}m²".format(larg, alt, area))
qdtTinta = area / 2

print("Voce precisa de {:.2f}l de tinta para pintar uma parede de {}m²".format(qdtTinta, area))

