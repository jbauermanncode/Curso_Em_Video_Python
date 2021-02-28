'''
    Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária pra pintá-la, sabendo que cada litro de tinta, pinta uma área de 2 metros quadrados.
'''
#Ler largura e altura
l = float(input('Digite a largura: '))
a = float(input('Digite a altura: '))

# Calcular a área
area = l * a

# Calcular a quantidade de tinta
t = area / 2

# Imprimir na Tela
print('A largura é {:.2f}.'.format(l))
print('A altura é {:.2f}.'.format(a))
print('A área é {:.2f}.'.format(area))
print('A quantidade de tinta usada é {:.2f} litros.'.format(t))