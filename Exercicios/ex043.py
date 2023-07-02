"""
Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
calcule seu Índice de Massa Corporal (IMC)
e mostre seu status, de acordo com a tabela abaixo:
    * IMC abaixo de 18,5: Abaixo do Peso
    * Entre 18,5 e 25: Peso Ideal
        – 25 até 30: Sobrepeso
        – 30 até 40: Obesidade
        – Acima de 40: Obesidade Mórbida
"""
altura = float(input("Digite sua altura: (utilize . e não , para separar as casas decimais) (Kg) "))
peso = float(input("Digite seu peso: (utilize . e não , para separar as casas decimais) (m) "))

imc = peso / (altura * altura)
print("Altura: {:.2f}m".format(altura))
print("Peso: {:.2f} kg".format(peso))
print("O seu IMC está em  {:.2f} kg/m²".format(imc))
print("Isso significa que: ")

if imc < 18.5:
    print("Você está abaixo do peso ideal")
    print("Procure um médico, pois isso não é saudavel")
elif imc >= 18.5 and imc < 25:
    print("Você está com o peso ideal")
elif imc >= 25 and imc < 30:
    print("Você está ACIMA do peso")
    print("Cuide-se")
elif imc >= 30 and imc < 40:
    print("Voce está com um certo grau de obesidade")
    print("Procure ajuda!")
else:
    print("Você está com um grau de Obesidade Mórbida")
    print("Procure ajuda.")
