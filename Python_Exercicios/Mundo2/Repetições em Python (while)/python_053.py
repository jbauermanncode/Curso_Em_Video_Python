'''
    Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
'''
# Importar função randint do módulo random
from random import randint

# Contador de tentativas
contador = 0

# Número que o computador pensa
computador = randint(0 , 5)
print('-=-'*20)
print('Olá! Pensei em um número de 0 a 10. Consegue adivinhar?')
print('-=-'*20)
# A tentativa do jogador de adivinhar
jogador = int(input('Em que número eu pensei? '))
print('###'*20)

# Laço while até o jogador acertar
while computador != jogador:
    jogador = int(input('Tente no novamente: '))
    contador += 1
    # Estrutura Condicional if/else
    if jogador == computador:
        print('____PARABÉNS! Você VENCEU!!!____')
    elif jogador > 10:
        print('Você é muito burro! Eu disse de 0 a 5. Acabou o jogo!')

# Imprimir o número que o computador pensou
print('Você precisou de {} tentativas.'.format(contador))
print('###'*20)

