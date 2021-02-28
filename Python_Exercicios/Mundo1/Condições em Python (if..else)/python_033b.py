'''
    Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
'''
# Ler 3 números
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))

# Estrutura Condicional if/else número menor
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3

print('O menor valor digitado foi {}'.format(menor))

# Estrutura Condicional if/else número maior
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3

print('O maior valor digitado foi {}'.format(maior))
