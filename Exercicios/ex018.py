"""Faça um programa que leia um ângulo qualquer e 
mostre na tela o valor do seno, cosseno e tangente desse ângulo."""
import math

ang = float(input("Digite um ângulo qualquer: (Utilize ponto e não vírgula.) "))

sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tang = math.tan(math.radians(ang))


print("Voce digitou: {} " .format(ang))
print("O SENO de {} é {:.2f}".format(ang, sen))
print("O COSSENO de {} é {:.2f}".format(ang, cos))
print("A TANGENTE de {} é {:.2f}".format(ang, tang))

