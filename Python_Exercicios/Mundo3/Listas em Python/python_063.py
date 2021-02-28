'''
    Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
'''
# Indicar uma lista
valores = list()

# Usar o laço for para ler numeros
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
# Usar o laço for para ver o numero e a posição
for p, v in enumerate(valores):
    # Procurar o numero maior usando max e imprimir na tela
    if v == max(valores):
        print(f'O maior valor é {v} e a posição é {(p) + 1}!')
    # Procurar o numero menor usando min e imprimir na tela
    if v == min(valores):
        print(f'O menor valor é {v} e a posição é {(p) + 1}!')