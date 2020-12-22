'''
    Sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
'''
# Importar Biblioteca Random
from random import shuffle

# Leia os 4 nomes
n1 = str(input('Digite um nome: '))
n2 = str(input('Digite um nome: '))
n3 = str(input('Digite um nome: '))
n4 = str(input('Digite um nome: '))

# Lista de alunos
lista = [n1, n2, n3, n4]

# Embaralhar a lista
shuffle(lista)

# Imprimir
print('A ordem de apresentação é: {}.'.format(lista))