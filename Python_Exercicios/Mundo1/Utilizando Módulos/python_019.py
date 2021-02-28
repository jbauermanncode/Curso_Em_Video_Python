'''
    Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.
'''
# Importar o randomizador de elementos
from random import choice

# Leia os 4 nomes
n1 = str(input('Digite um nome: '))
n2 = str(input('Digite um nome: '))
n3 = str(input('Digite um nome: '))
n4 = str(input('Digite um nome: '))

# Fazer uma lista 
lista = [n1, n2, n3 ,n4]

# Sortear um nome da lista
escolhido = choice(lista)

# Imprimir
print('O aluno escolhido foi {}.'.format(escolhido))

