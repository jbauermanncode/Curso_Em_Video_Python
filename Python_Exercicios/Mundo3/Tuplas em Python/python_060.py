'''
    Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9.

B) Em que posição foi digitado o primeiro valor 3.

C) Quais foram os números pares.
'''
# Fazer uma Tupla ler 4 números
n = (int(input('Digite um número: ')),
     int(input('Digite outro número: ')),
     int(input('Digite um número: ')),
     int(input('Digite um número: ')))
print(f'Você digitou os valores {n}.')

# Contar as vezes que aparece o 9
if 9 in n:
    print(f'O numero 9 aparece {n.count(9)} vezes')
else:
    print('O valor 3 não foi digitado')
# Posição do numero 3
if 3 in n:
    print(f'O numero 3 apareceu na {n.index(3)+1}ª posição.')
else:
    print('O valor 3 não foi digitado')

# Para saber os numeros pares
print('Os valores pares digitados foram: ', end='')
for par in n:
    if n % 2 == 0:
        print(n, end=' ')
    else:
        print('Nenhum número par foi digitado.')

