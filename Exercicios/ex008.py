"""
Faça um programa que lei uma media em metros
e em seguida converta para centimetro e depois em milimetros
"""

metro = float(input("digite a medida que vc deseja converter: "))
decimetro = metro * 10
centimetro = metro * 100
milimetro = metro * 1000
decametro = metro / 10
hectometro = metro / 100
kilometro = metro / 1000

print("Voce digitou {} metros, \nque vale {} cm \n {} mm".format(metro, centimetro, milimetro))
print("{}Dm {}Hm {}Km" .format(decametro, hectometro, kilometro))