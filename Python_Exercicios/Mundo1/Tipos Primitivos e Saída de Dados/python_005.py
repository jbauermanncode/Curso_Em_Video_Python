'''
  Faça um programa que leia um número Inteiro e mostre
  na tela o seu sucessor e seu antecessor.
'''
# Ler um número Inteiro
n = int(input('Digite um número: '))

# Imprimir na tela
print(n)
print('O sucessor de {} é {}.'.format(n, (n + 1)))
print('O antecessor de {} é {}.'.format(n, (n - 1)))