'''
    Crie um programa que faça o computador jogar Jokenpô com você.
'''
from random import randint
# Esperando 1 segundo dizendo Jokenpo
from time import sleep

# Fazer uma Lista
itens = ('Pedra', 'Papel', 'Tesoura')

computador = randint(0, 2)

print('[0] PEDRA: ')
print('[1] PAPEL: ')
print('[2] TESOURA: ')
jogador = int(input('Escolha: '))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)

print('-='*40)
print('A escolha do usuário foi {} e a escolha do computador foi {}.'.format(itens[jogador], itens[computador]))
print('-='*40)

if computador == 0:
    if jogador == 0:
        print('EMPATE')
    
    elif jogador == 1:
        print('Jogador VENCE!')
    
    elif jogador == 2:
        print('Computador VENCE!')
    
    else:
        print('Jogada Inválida!')

if computador == 1:
    if jogador == 0:
        print('Computador VENCE!')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('Jogador VENCE!')
    else:
         print('Jogada Inválida!')

if computador == 2:
    if jogador == 0:
        print('Jogador VENCE!')
    elif jogador == 1:
        print('Computador VENCE!')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('Jogada Inválida!')


