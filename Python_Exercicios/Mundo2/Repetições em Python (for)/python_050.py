'''
    Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
'''
# Importar o ano atualizado do datatime.
from datetime import date
ano_atual = date.today().year

# Contadores
menor = 0
maior = 0

# Laço for para ler o nome de sete pessoas

for p in range(1 , 8):
    ano_nascimento = int(input('Qual o ano de nascimento: '))
    if  ano_atual - ano_nascimento < 18:
        
        menor = menor + 1

    elif ano_atual - ano_nascimento > 18:
        
        maior = maior + 1

print('O número de pessoas que atingiram a maioridade é {}.'.format(maior))
print('O número de pessoas que não atingiram a maioridade é {}.'.format(menor))
print('FIM!')