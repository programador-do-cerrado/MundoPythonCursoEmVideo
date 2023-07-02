"""
Escreva um programa para aprovar o empréstimo bancário
para a compra de uma casa.
Pergunte:
    * o valor da casa,
    * o salário do comprador
    * e em quantos anos ele vai pagar.
A prestação mensal não pode exceder 30% do salário
ou então o empréstimo será negado.
"""
print("Simulador de financiamento. ")

nome = str(input("Nome: "))
valCasa = float(input("Valor da casa: R$"))
salario = float(input("Salário R$: "))
tempo = int(input("Em quantos anos pretende pagar: "))
meses =  tempo * 12
prestacao = valCasa / meses

print("Cliente: {}".format(nome))
print("Valor da casa: R${:.2f}".format(valCasa))
print("Salario: R${:.2f}".format(salario))
print("Número de prestações: {} ".format(meses))
print("Valor das prestações: R${:.2f}.".format(prestacao))

if prestacao >= (salario * 0.3):
    print("Financiamento não autorizado, pois o valor das prestações R${:.2f} exede '30%' do seu salário {:.2f}".format(prestacao, salario))
else:
    print("Financiamento autorizado.")
    print("Salario: R${:.2f}".format(salario))
    print("Valor das prestações: R${:.2f}.".format(prestacao))    
