"""
Faça um programa que leia o ano de nascimento de um jovem
e informe, de acordo com a sua idade,
    * se ele ainda vai se alistar ao serviço militar,
    * se é a hora exata de se alistar
    * ou se já passou do tempo do alistamento.
Seu programa também deverá
    * mostrar o tempo que falta ou que passou do prazo.
"""
from datetime import date
nascimento = int(input("Digite o ano que você nasceu: (AAAA) "))
anoCorrente = date.today().year

idade = anoCorrente - nascimento
tempoRestante = 18 - idade

print("{}, esse ano voce completa {} anos".format(nome, idade))
if idade < 18:
    ano = anoCorrente + tempoRestante
    print("Você ainda não está na idade para se alistar. ")
    print("Falta(m) {} ano(s)".format(tempoRestante))
    print("Apresente-se em {}".format(ano))
elif idade == 18:
    print("Você deve se alistar esse ano")
else:
    tempoRestante = tempoRestante * (-1)
    ano = anoCorrente - tempoRestante
    print("Você tem anos {} e está atrasado {} anos".format(idade, tempoRestante))
    print("Você deveria ter se apresentado em {}. ".format(ano))
