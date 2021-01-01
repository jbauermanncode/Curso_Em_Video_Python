'''
    Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
'''
# Importar radint de random
from random import randint

# Escolha Par ou Impar
print('++++ Escolha Par ou Ímpar ++++')
print('**'*20)
print('[1] Ímpar ')
print('[2] Par ')


# Usar randint para o computador escolher um numero aleatório
computador = randint(0, 11)

# Contador de vitórias
vitoria = 0

# Laço while para fazer o jogo e descobrir quem venceu
while True:
    jogador = int(input('Digite um 1 ou 2 : '))
    # Escolhendo Par
    if jogador == 2:
        n = int(input('Digite um número : '))
        soma = n + computador
        if soma % 2 == 0:
            print('-=='*20)
            print('Você VENCEU!!!')
            print('-=='*20)
            print(f'O computador escolheu {computador}, e o jogador escolheu {n}.')
            print('-=='*20)
        elif soma % 2 != 0:
            print('-=='*20)
            print('Você PERDEU!!!')
            print(f'O computador escolheu {computador}, e o jogador escolheu {n}.')
            # Quebrar o laço
            break
    # Escolhendo Impar
    if jogador == 1:
        n = int(input('Digite um número :'))
        soma = n + computador
        if soma % 2 != 0:
                print('-=='*20)
                print('Você VENCEU!!!')
                print('-=='*20)
                print(f'O computador escolheu {computador}, e o jogador escolheu {n}.')
                print('-=='*20)
        elif soma % 2 == 0:
            print('-=='*20)
            print('Você PERDEU!!!')
            print(f'O computador escolheu {computador}, e o jogador escolheu {n}.')
            # Quebrar o laço
            break
    vitoria += 1
print(f'O número de vitórias consecutivas do jogador foi {vitoria}.')
print('-=='*20)
print('FIM DE JOGO')