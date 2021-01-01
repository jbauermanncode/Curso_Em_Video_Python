'''
    Faça um programa que leia um número qualquer e mostre o seu fatorial. 
    Exemplo:

    5! = 5 x 4 x 3 x 2 x 1 = 120
'''
# Ler um número
n = int(input('Digite um número: '))

c = n

fatorial = 1

print('Calculando {}! = '.format(n), end='')

# Laço while para fazer o fatorial
while c > 0:
    print('{}'.format(c), end='')
    print(' X ' if c > 1 else ' = ', end='')
    fatorial *= c
    c -= 1
print('{}'.format(fatorial))
    
    
