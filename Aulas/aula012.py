"""
Condições aninhadas
"""
nome = str(input("Qual seu nome? "))
if nome == "Fernando":
    print("Que nome bonito")
elif nome == "Pedro" or nome == "Maria" or nome == "Paulo":
    print("Seu nome é bem nomral no Brasil")
elif nome in 'Ana Cláudia jessica Juliana':
    print("Que belo nome feminino")
else:
    print("Seu nome é bem normal.")
print("Tenha um bom dia, {}!".format(nome))
