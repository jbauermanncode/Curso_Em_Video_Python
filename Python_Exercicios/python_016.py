'''
    Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira
'''
# Importar a biblioteca math e floor
from math import floor

# Ler um número Real
n= float(input('Digite um número: '))

# Imprimir o número Inteiro
print('O número {} tem a parte inteira {}.' .format(n, floor(n)))


