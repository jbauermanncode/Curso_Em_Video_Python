'''
    Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
'''
# Importar função randint do módulo random
from random import randint

# Número que o computador pensa
computador = randint(0 , 5)
print('-=-'*20)
print('Olá! Pensei em um número de 0 a 5. Consegue adivinhar?')
print('-=-'*20)
# A tentativa do jogador de adivinhar
jogador = int(input('Em que número eu pensei? '))
print('###'*20)

# Estrutura Condicional if/else
if jogador == computador:
    print('____PARABÉNS! Você VENCEU!!!____')
else:
    print('____HAHAHA! Você PERDEU!!!____')

# Imprimir o número que o computador pensou
print('Eu pensei no número {}'.format(computador))
print('###'*20)

