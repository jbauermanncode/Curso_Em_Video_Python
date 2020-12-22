'''
    Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.
'''
# Importar math
from math import hypot

# Leia os catetos
co= float(input('Valor do cateto oposto: '))
ca= float(input('Valor do cateto adjacente: '))

# Calcular Hipotenusa
h = hypot(co, ca)

# Imprimir a hipotenusa
print('O valor da hipotenusa é {:.2f}' .format(h))

