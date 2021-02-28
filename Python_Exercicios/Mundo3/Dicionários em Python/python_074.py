'''
    Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
'''
# Importar datetime para atualizar ano
from datetime import datetime

# Criar um dicionario para dados
dados = dict()

# Ler Dados
dados['nome'] = str(input('Nome: '))
# Sem cadastrar ano de nascimento
nasc = int(input('Ano de Nascimento:  '))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))

if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de Contratação: '))
    dados['salário'] = float(input('Salário: R$'))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - datetime.now().year)
print('-=' * 30)

# Fazer um for para imprimir os elementos
for k, v in dados.items():
    print(f'  -{k} tem o valor {v}')