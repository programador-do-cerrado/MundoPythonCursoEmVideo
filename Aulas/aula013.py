"""
Nessa aula, vamos começar nossos estudos com os laços e vamos fazer primeiro o “for”,
que é uma estrutura versátil e simples de entender. Por exemplo:
    for c in range(0, 4):
    print(c)
    print(‘Acabou’)
    Exemplos de código em python
    para criar laços de repetições
"""

print("Oi")
print("Oi")
print("Oi")
print("Oi")
print("Oi")
print("Oi")

# em vez disso -----------------------

for c in range(1, 6):
    print("Oi! dentro do laço ")
    print("Fim dentro do laço - cuidado com a identação.")
print("Fim. Fora do laço")

for d in range(1, 7):
    print(d)
    "Conta de 1 até 6 pois ele ignora o último valor"
print("Fim!")

for f in range(30, 0, -1):
    print("Contagem regressiva {}".format(f))

g = int(input('Digite um número: '))
for g in range(0, g + 1):
    print(g)

# _______________ Exemplo dado na aula


i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))

for q in range(i, f + 1, p):
    print(q)
    print("Um texto qualquer que vai se repetir dento do laço!")
print("Fim")

# ------------------- Somatório

s = 0
for x in range(0, 6):
    n = int(input('Digite um valor: '))
    s = s + n
print("O somatório de todos os valores foi {}".format(s))
