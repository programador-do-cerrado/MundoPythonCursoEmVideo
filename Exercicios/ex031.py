"""
Desenvolva um programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km
e R$0,45 parta viagens mais longas.
"""
distancia = float(input("Digite a distância do seu local de destino:(utilize ponto e não vírgula). "))

if (distancia <= 200):
    valor = distancia * 0.50
    print("O seu destino fica a {:.1f}Km, portanto o valor da passagem é de R$ {:.2f}".format(distancia, valor))
else:
    valor = distancia * 0.45
    print("O seu destino fica a {:.1f}Km, portanto o valor da passagem é de R$ {:.2f}".format(distancia, valor))
print("Boa viagem")