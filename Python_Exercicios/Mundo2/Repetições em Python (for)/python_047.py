'''
    Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
'''
# Ler o primeiro ter a razão
pt = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
contador = 0
for i in range(pt, 100, r):
    contador = contador + 1
    if contador <= 10:
        print('-> ', end='')
        print(i, end=' ')
        
print('Acabou!')
