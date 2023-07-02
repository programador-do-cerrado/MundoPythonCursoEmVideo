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
    print("Você vai pagar à vista: dinheiro/cheque.")
    print("O seu produto custaria R$ {:.2f}, com '10%' de desconto: R$ {:.2f}".format(valorInicial, valorFinal))
elif opcao == 2:
    valorFinal = valorInicial - (valorInicial * (5 / 100))
    print("Você vai pagar à vista: cartão.")
    print("O seu produto custaria R$ {:.2f}, com '5%' de desconto: R$ {:.2f}".format(valorInicial, valorFinal))
elif opcao == 3:
    prestacao = valorInicial / 2
    print("Você vai pagar à vista: cartão.")
    print("O seu produto custou R$ {:.2f}, em 2X de R$ {:.2f}".format(valorInicial, prestacao))
elif opcao == 4:
    nparcelas = int(input("Em quantas vezes: "))
    valorFinal = valorInicial + (valorInicial * (20 / 100))
    prestacao = valorFinal / nparcelas
    print("Você vai pagar em {}X no cartão.".format(nparcelas))
    print("O seu produto custaria R$ {:.2f}, passou a custar R$ {:.2f} em {}X de R$ {:.2f}".format(valorInicial,
                                                                                                   valorFinal,
                                                                                                   nparcelas,
                                                                                                   prestacao))
