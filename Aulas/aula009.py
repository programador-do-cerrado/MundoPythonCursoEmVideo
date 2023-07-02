from builtins import print

from _testcapi import frame_new

frase = str("Curso em vídeo Python")
frase2= str("   Aprenda Python  ")


#Com esse comando vai imprimir a string toda
print(frase)

# com esse comando vai imprimir o caracter naposição 9
print(frase[9])

# com esse comando vai imprimir apartir do 9 até o 13, pois o 14 será excluído
print(frase[9:14])
print(frase[9:21])
print(frase[9:22])

# com esse comando vai imprimir apartir do 9 até o 21, excluido o 21 e pulando de 2 em 2
print(frase[9:21:2])

# com esse comando vai imprimir apartir do começo até o 4, excluindo o 5
print(frase[:5])
print(frase[:9])

# com esse comando vai imprimir apartir do 9 até o último caracter
print(frase[15:])

print(frase[4::3])

print(frase)
print(len(frase))
print(frase.count('o'))
print(frase.count('o', 0, 13))
print(frase.find('deo'))

""" Por não haver android na frase, vai retornar -1, 
e com isso é possível fazer algo com boolean, retornando um false """
print(frase.find('Android'))

print(frase.replace('Python', 'Android'))
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())
print(frase2.strip())
print(frase2.rstrip())
print(frase2.lstrip())

print(frase.split())
print('-'.join(frase))

"__________________________Práticas_________________________"

