'''
    Escreva um programa que leia dois números inteiros e compare- os, mostrando na tela uma mensagem:

    - O primeiro valor é maior
    
    - O segundo valor é maior

    - não existe valor maior, os dois são iguais
'''
# Ler dois números inteiros
n1 = int(input('Informe o primeiro número: '))
n2 = int(input('Informe o segundo número: '))

# Operadores Lógicos
n1_maior = n1 > n2
n2_maior = n2 > n1

# Estrutura Condicional if, elif, else.
if n1_maior:
    print('O número {} é o maior!'.format(n1))

elif n2_maior:
    print('O número {} é o maior!'.format(n2))

else:
    print('Os números são iguais!')
    