'''
    Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último separadamente.
'''
# Leia o nome de uma pessoa
n = str(input('Escreva o nome: ')).strip()

# Separar o nome em partes
nome = n.split()

# Imprimir 
print(n)

print('O seu primeiro nome é {}.'.format(nome[0]))

print('O seu último nome é {}.'.format(nome[len(nome) - 1]))
