wordTest = input('Digite algo: ' )
print("O tipo primitivo desse valor é: ", type(wordTest))
print("Só tem espaços?",wordTest.isspace())
print("É um número? ", wordTest.isnumeric())
print("É alfabético? ", wordTest.isalpha())
print("É alfanumerico? ", wordTest.isalnum())
print("É maiusculo? ", wordTest.isupper())
print("É minusculo? ", wordTest.islower())
print("Está capitalizada? ", wordTest.istitle())

