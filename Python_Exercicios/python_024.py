'''
    Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".
'''
# Leia o nome de uma cidade
cidade = str(input('Digite o nome de uma cidade: ')).strip()

# Imprimir na tela
print('santo' in cidade[:5].lower())

# Imprimir outra maneira
print(cidade[:5].upper() == 'SANTO')
