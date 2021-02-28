'''
    Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
'''
# Importar randint de random para pegar numeros aleatórios. E importar sllep de time para esperar um tempo de um jogador para outro. Importar itemgetter para organizar o ranking.
from random import randint
from time import sleep
from operator import itemgetter

# Criar um dicionário chamado jogo
jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)}

# Criar um dicionario para rankear os jogadores.
ranking = list()

print('Valores sorteados:')
# Para formatar um print usando for
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(2)

ranking = sorted(jogo.items(), key=itemgetter(1), reverse = True)

print('-=' * 30)
print(' === Ranking dos Jogadores ===')

for i, v in enumerate(ranking):
    print(f'    {i+1}º lugar: {v[0]} com {v[1]}.')
    sleep(2)


# 