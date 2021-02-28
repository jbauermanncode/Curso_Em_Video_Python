'''
    Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.
'''
# Criar uma função para calcular a area, que recebera dois parametros l = largura e c = comprimento.
def area(l, c):
    a = l * c
    print(f'A área de um terreno {l} x {c} é de {a}m².')


# Programa Principal
print(' Controle de Terrenos')
print('_'* 20) 
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))  
area(l, c)