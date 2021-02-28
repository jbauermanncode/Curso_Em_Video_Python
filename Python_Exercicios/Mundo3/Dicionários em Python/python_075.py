'''
    Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
'''
# Fazer um diiconario para jogador
jogador = {}

# Fazer uma lista para partidas
partidas = list()

# Ler nome do jogador 
jogador['nome'] = str(input('Nome do Jogador: '))
tot_partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

# Fazer um for para acrescentar partidas no histórico do jogador 
for c in range(0, tot_partidas):
    partidas.append(int(input(f'  Qunatos gols na partida {c +1} fez? ')))

# Passar lista para o dicionario e fazer cópias da lista
jogador['gols'] = partidas[:]
jogador['total_gols'] = sum(partidas)

print('-=' * 30)
print(jogador)
print('-=' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')
print('-=' * 30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')

for i, v in enumerate(jogador['gols']):
    print(f'   => Na partida {i + 1}, fez {v} gols.')
print(f'Foi um total de {jogador["total_gols"]} gols.')