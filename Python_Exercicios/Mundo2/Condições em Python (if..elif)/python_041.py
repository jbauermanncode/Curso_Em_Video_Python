'''
    Crie um programa que faça o computador jogar Jokenpô com você.
'''
# Para o computador escolher uma string
from random import randint

# Esperando 1 segundo dizendo Jokenpo
from time import sleep

# Ler uma palavra
print('[1] PEDRA: ')
print('[2] PAPEL: ')
print('[3] TESOURA: ')
usuario = int(input('Escolha: '))
if usuario == 1:
    usuario = 'PEDRA'
elif usuario == 2:
    usuario = 'PAPEL'
elif usuario == 3:
    usuario = 'TESOURA'

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)

# O computador escolherá uma palavra aleatoriamente

escolha = randint(1, 3)
if escolha == 1:
    escolha = 'PEDRA'
elif escolha == 2:
    escolha = 'PAPEL'
elif escolha == 3:
    escolha = 'TESOURA'

# Jogando com o computador
print('A escolha do usuário foi {} e a escolha do computador foi {}.'.format(usuario, escolha))

usuario_vencedor = (usuario == 'PEDRA' and escolha == 'TESOURA') or (usuario == 'PAPEL' and escolha == 'PEDRA') or  (usuario == 'TESOURA' and escolha == 'PAPEL')
empate = usuario == escolha
print()
print('-=='*10)
if empate:
    print('O JOGO EMPATOU!')
elif usuario_vencedor:
    print('O jogador VENCEU!!!')
else:
    print('O computador VENCEU!!!')
print('-=='*10)