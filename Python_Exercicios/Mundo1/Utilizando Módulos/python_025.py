'''
    Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
'''
# Ler o nome completo de uma pessoa
nome = str(input('Digite o nome: '))

# Imprimir nome
print('silva' in nome.lower())