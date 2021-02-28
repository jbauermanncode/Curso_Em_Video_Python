'''
    Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.
'''
# Acumulador para fazer a soma total
s = 0

# Contador para ver quantos números foram somados
c = 0

# Laço for para saber os números múltiplos de 3 a partir do número 1 até o 50.
for i in range(1, 501, 2):
    if i % 3 == 0:
        c = c + 1
        s = s + i
     
print('A soma de todos os multiplos de 3 ímpares é {}, e foram contados {} números.'.format(s, c))

