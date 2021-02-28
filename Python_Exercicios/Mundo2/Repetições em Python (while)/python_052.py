'''
    Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto.
'''
n = 'Augusto'

if n in 'aeiou' :
    print('sim')
# Ler o nome e o sexo de uma pessoa
nome = str(input('Nome: '))
sexo = str(input('Sexo: ')).strip().upper()[0]
idade = int(input('Idades: '))

# Laço while para digitar novamente se a pessoa escrever errado
while sexo not in 'MmFf':
    sexo = str(input('Digite novamente o sexo: ')).strip().upper()[0]

print('O seu nome é {}, e o seu sexo é {}.'.format(nome, sexo))

