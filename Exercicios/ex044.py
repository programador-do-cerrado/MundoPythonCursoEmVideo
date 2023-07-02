"""
Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal
e condição de pagamento:
    – à vista dinheiro/cheque: 10% de desconto
    – à vista no cartão: 5% de desconto
    – em até 2x no cartão: preço formal
    – 3x ou mais no cartão: 20% de juros
    """
valorInicial = float(input("Digite o valor do produto R$ "))
print("Digite a forma de pagamento: ")
print("[ 1 ] à vista dinheiro/cheque: 10% de desconto.")
print("[ 2 ] à vista no cartão: 5% de desconto.")
print("[ 3 ] em até 2x no cartão: preço formal")
print("[ 4 ] 3x ou mais no cartão: 20% de juros")

opcao = int(input("Digite sua opção (1 - 4): "))

if opcao == 1:
    valorFinal = valorInicial - (valorInicial * (10 / 100))
    print("Você vai pagar à vista.")
    print("O seu produto custaria R$ {:.2f}, e passou a custar {:.2f}".format(valorInicial, valorFinal
                                                                              ))
