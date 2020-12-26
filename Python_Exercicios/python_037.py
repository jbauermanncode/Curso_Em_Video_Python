'''
    Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
'''

# Ler um número inteiro e definr a base

n = int(input('Digite um número: '))

base = int(input('Em qual base será feita a conversão? '))
print('[1] Para Binário')
print('[2] Para Octal')
print('[3] Para Hexadecimal')

# Conversão para binário, hexadecimal, octal, com Estrutura Condicional if, elif, else.
if base == 1:
    print('O número {}, fica {} em binário.'.format(n, bin(n)[2:]))
elif base == 2:
    print('O número {}, fica {} em octal.'.format(n, oct(n)[2:]))
elif base == 3:
    print('O número {}, fica {} em hexadecimal.'.format(n, hex(n)[2:]))
else:
    print('O número de base não está listado')