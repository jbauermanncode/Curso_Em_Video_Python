'''
    Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
'''
# Leia um número
num = int(input('Informe um número: '))

# Descobrir a Unidade
u = num // 1 % 10

# Descobrir a Dezena
d = num // 10 % 10

# Descobrir a Centena
c = num // 100 % 10

# Descobrir o Milhar
m = num // 1000 % 10

# Imprimir na tela
print('Analisando o número {}.'.format(num))

print('Unidade: {}.'.format(u))

print('Dezena: {}'.format(d))

print('Centena: {}.'.format(c))

print('Milhar: {}.'.format(m))