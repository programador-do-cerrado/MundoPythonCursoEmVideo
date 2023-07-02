"""
Crie um programa que leia duas notas de um aluno e calcule sua média,
mostrando uma mensagem no final, de acordo com a média atingida:
    * Média abaixo de 5.0: REPROVADO
    * Média entre 5.0 e 6.9: RECUPERAÇÃO
    * Média 7.0 ou superior: APROVADO

"""
n1 = float(input("Nota 1: (Use ponto para separar as casas decimais) "))
n2 = float(input("Nota 2: (Use ponto para separar as casas decimais) "))

media = (n1 + n2) / 2

print("Você tirou {:.2f} e {:.2f} ".format(n1, n2))
print("Sua média foi: {:.2f}".format(media))
if media < 5:
    print("REPROVADO")
elif media == 5 or media < 6.9:
    print("RECUPERAÇÃO")
else:
    print("APROVADO")
