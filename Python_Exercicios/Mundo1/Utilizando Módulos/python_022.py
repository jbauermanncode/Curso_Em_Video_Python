'''
    Crie um programa que leia o nome completo de uma pessoa e mostre:
        - O nome com todas as letras maiusculas e minusculas.
        - Quantas letras ao todo (sem considerar espaços).
        - Quantas letras tem o primeiro nome.
'''
# Ler o nome completo
nome = str(input('Digite o seu nome: ')).strip()

# Imprimir o nome completo
print(nome)

# Imprimir com letras maiusculas
print('O nome com todas as letras maiusculas')
print(nome.upper())

# Imprimir com letras minusculas
print('O nome com todas as letras minusculas.')
print(nome.lower())

# Imprimir quantidade de letras ao todo (sem considerar espaços).
print('Quantas letras ao todo (sem considerar espaços).')
print(len(nome)-nome.count(' '))

# Imprimir quantas letras tem no primeiro nome.
print('Quantas letras tem o primeiro nome.[Parte 1]')
print(nome.find(' '))

# Outra maneira de fazer quantas letras tem no primeiro nome.
print('Quantas letras tem o primeiro nome.[Parte 2]')
separa = nome.split()
print(len(separa[0]))


