'''
    Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.
'''
# Fazer um dicionario para aluno
aluno = dict()

# Pedir nome e média do aluno
aluno['nome'] = str(input('Nome: '))
aluno['média'] = float(input(f'Média de {aluno["nome"]}: '))

# Definir a situação do aluno em relação a média
if aluno['média'] >= 7:
    aluno['situação'] = 'Aprovado'
elif 5 <= aluno['média'] < 7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'

print('-=' * 30)
# Fazer um for para imprimir na tela
for k, v in aluno.items():
    print(f'{k} é igual a {v}.')
