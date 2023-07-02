"""
Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7,00 por cada Km acima do limite.
"""
velocidade = float(input("Digite a velocidade que o carro passou."))
excesso = velocidade - 80
valorMulta = excesso * 7

if (velocidade > 80):
    print("Você foi multado, devido a sua alta velocidade.")
    print("Você estava a {}KM/h, você excedeu {:.0f}KM/h, portanto sua multa é de R${:.2f}".format(velocidade, excesso,  valorMulta))
else:
    print("Parabens por respeitar os limites de velocidade. Boa viagem")
print("Tenha um bom dia, dirija com segurança")


