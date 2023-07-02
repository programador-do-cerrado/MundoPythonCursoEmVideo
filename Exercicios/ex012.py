"""
Faça um algoritmo que leia o preço de um produto e mostre seu novo preço,
com 5% de desconto.
"""

valorCheio = float(input("Digite o valor do produto: R$ "))
valorDesc = valorCheio - (valorCheio * (5/100))
print("A sua compra de R${:.2f}, com 30% de desconto, ficou R${:.2f}".format(valorCheio, valorDesc))
