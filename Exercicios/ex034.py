"""
Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$1250,00, calcule um aumento de 10%.
Para os inferiores ou iguais, o aumento é de 15%.
"""

salário = float(input("Digite o valor do salário: (utilize . e não, para separar os centavos). R$ "))

if salário >= 1250:
    reajuste = salário + (salário * (10 / 100))
    print("O seu salário é de R$ {:.2f}, com o reajuste passará a ser R$ {:.2f}".format(salário, reajuste))
else:
    reajuste = salário + (salário * (15 / 100))
    print("O seu salário é de R$ {:.2f}, com o reajuste passará a ser R$ {:.2f}".format(salário, reajuste))
