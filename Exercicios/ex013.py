"""
Faça um algoritmo que leia o salário de um funcionário
e mostre seu novo salário, com 15% de aumento.
"""

salario = float(input("Qual é o salário do funcionário? R$: "))
reajuste = salario + (salario * (15/100) )
print("O salário atual é de R${:.2f}, com o reajuste passará ser R${:.2f}." .format(salario, reajuste))
