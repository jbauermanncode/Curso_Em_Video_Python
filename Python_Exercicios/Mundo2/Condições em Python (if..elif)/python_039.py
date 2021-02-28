'''
    Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
'''
# Importar datatime para atualizar o ano
from datetime import date
# Ler o ano de nascimento
nascimento = int(input('Em que ano você nasceu? '))

# Calcular a idade
atual = date.today().year
idade = atual - nascimento
print('A sua idade é {} anos.'.format(idade))

# Estrutura Condicional if, elif, else
if idade == 18:
    print('Você deve se alistar!')
elif idade < 18:
    print('Você deve se alistar daqui {} anos!'.format(18 - idade))
else:
    print('Você se alistou, ou deveria ter se alistado a {} anos!'.format(idade - 18))
