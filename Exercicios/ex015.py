"""
Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar,
sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
"""

dias = int(input("Quantos dias o carro ficou alugado: "))
km = float(input("QUantos kilometros percorridos: "))

kilometragem = km * 0.15
diariasTotal = dias * 60
valorPago = kilometragem + diariasTotal

print(
    "O carro foi alugado por {} dias e percorreu um distancia de {} km, portanto o valor pago será de R${:.2f}.".format(
        dias, km, valorPago))
print("Sendo R${:.2f} de kilometragem e R${:.2f} de diaria".format(kilometragem, diariasTotal))
