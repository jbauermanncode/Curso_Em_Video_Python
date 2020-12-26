'''
    Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
'''
# Ler um número inteiro
n = int(input('Digite um número: '))
contador = 0
#Laço for para fazer a divisão e saber por quantos números é divisivel
for c in range(1, n+1):
    if n % c == 0:
        print('\033[1;34m', end=' ')
        contador += 1
    
    else:
        print('\033[31m', end=' ')

    print('{}'.format(c), end=' ')
print('\n\033[mO número {} foi divisível {} vezes.'.format(n, contador))

# Para saber se o número é primo
if contador == 2:
    print('E por isso ele é primo!')
else:
    print('E por isso ele não é primo!')