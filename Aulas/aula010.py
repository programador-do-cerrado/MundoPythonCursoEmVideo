tempo = int(input("QUantos anos tem seu carro?: "))
if tempo <= 3:
    print("Carro novo")
else:
    print("Carro velho")
print("--FIM--")
print('carro novo em uma linha de cmd' if tempo <= 3 else 'carro velho em uma linha de cmd')
print("--FIM--")
print("--" * 25)

n1 = float(input("Digite a nota do 1º bimestre: "))
n2 = float(input("Digite a nota do 2º bimestre: "))
media = (n1 + n2) / 2
print("Sua média final é {:.1f}.".format(media))
if media >= 5:
    print("Aprovado. ")
else:
    print("Reprovado.")