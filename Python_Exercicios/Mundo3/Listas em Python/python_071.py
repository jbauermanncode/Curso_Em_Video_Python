'''
    Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.

    mostre na tela:
      A) A soma de todos os valores pares digitados.                            B) A soma dos valores da terceira coluna.  
      C) O maior valor da segunda linha.

    
'''
# Fazer a lista da matriz
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# Declarar Variaveis
soma_par = maior = soma_coluna = 0

# Fazer um laço dentro do outro para suprir todas as colunas
# laço for para as linhas
for l in range(0, 3):
    #laço for para as colunas
    for c in range(0, 3):
        matriz[l][c] = int(int(input(f'Digite um valor para [{l}, {c}]: ')))
print('-='* 30)

# Fazer novamente um for com a linha dentro da coluna para mostrar a estrutura na tela
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        # verificar se um numero é par e fazer a soma quando for
        if matriz[l][c] % 2 == 0:
            soma_par += matriz[l][c]
        
    print()
print('-='*30)
print(f'A soma dos valores pares é {soma_par}!')

# Fazer um for somente para a coluna e não para a linha
for l in range(0, 3):
    soma_coluna += matriz[l][2]
print(f'A soma dos valores da terceira coluna é {soma_coluna}!')

# fazer um for somente para a linha e não para a coluna
for c in range(0, 3):
    if c == 0:
        maior = matriz[1][c]
    elif matriz[1][c] > maior:
        maior = matriz[1][c]
print(f'O maior valor da segunda linha é {maior}!')