'''
    Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
'''
# # Média das idades
soma_idade = 0
media_idade = 0

# Homem mais velho
maior_idade_homem = 0
nome_velho = ''

# Quantidade de mulheres que tem menos de 20 anos
total_mulheres20 = 0

# Fazer um laço for para ler o nome de 4 pessoas
for c in range(1, 5):
    print('----- {}ª PESSOA -----'.format(c))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    soma_idade += idade
    
    # Para saber qual homem mais velho
    if c == 1 and sexo in 'Mm':
        maior_idade_homem = idade
        nome_velho = nome
    if sexo in 'Mm' and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_velho = nome
    if sexo in 'Ff' and idade < 20:
        total_mulheres20 += 1

# Calcular a média de idade
media_idade = soma_idade / 4
print('A média de idade do grupo é de {} anos.'.format(media_idade))
print('O homem mais velho tem {} anos e se chama {}.'.format(maior_idade_homem, nome_velho))
print('A quantidade de mulheres com menos de 20 anos é de {}.'.format(total_mulheres20))