'''
    Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
'''
# Importar a função date do módulo datetime
from datetime import date

# Ler ano
ano = int(input("Que ano você quer analisar? Coloque 0 para analisar: "))

# Para saber sobre o ano atual
if ano == 0:
    ano = date.today().year

# Estrutura Condicional if/else
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é BISSEXTO.'.format(ano))
else:
    print('O ano {} não é BISSEXTO.'.format(ano))
