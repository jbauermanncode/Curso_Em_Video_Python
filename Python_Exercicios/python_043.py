'''
    Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.
'''
# Laço for para descobrir os numeros pares
for i in range(1 + 1, 51, 2):# 1 + 1 para a contagem começar a partir de 2
    print(i)
print('Esses são os números pares de 1 a 50.')
print()
print('**'*40)
print()

# Outra maneira de fazer
for i in range(1 , 51):
    print('.', end= '')
    if i % 2 == 0:
        print(i, end=' ')
print('Acabou')