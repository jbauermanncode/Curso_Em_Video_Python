'''
    Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
'''
# Importar math library
from math import radians, sin, cos, tan

# Leia o ângulo
angulo = float(input('Digite o valor de um ângulo: '))

# Calcular o seno
seno = sin(radians(angulo))

# Calcular o cosseno
cosseno = cos(radians(angulo))

# Calcular a tangente
tangente = tan(radians(angulo))

# Imprimir na tela
print('O ângulo de {} tem o SENO de {:.2f}.'.format(angulo, seno))
print('O ângulo de {} tem o COSSENO de {:.2}.'.format(angulo, cosseno))
print('O ângulo de {} tem a TANGENTE de {:.2f}.'.format(angulo, tangente))