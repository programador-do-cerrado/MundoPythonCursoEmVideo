"""Crie um programa que leia  quanto dinheiro uma pessoa tem na carteira e
mostre quantos Dólares ela pode comprar"""

BRL = float(input("Quantos reais vc tem? R$"))
cotacao = float(input("Qual a cotação do dolar hj?"))

USD = BRL / cotacao
print("Com R${:.2f} você pode comprar USD{:.2f} ".format(BRL, USD))
