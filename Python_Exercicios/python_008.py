'''
   Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e melimetros.
'''

# Leia um valor em metros
m = float(input('Digite um valor em metros: '))

# Converter para centimetros
c = float(m * 100)

# Converter para milimetros
mm = float(m * 1000)

# Imprimir na tela
print('{:.1f}m'.format(m))
print('{:.1f}cm'.format(c))
print('{:.1f}mm'.format(mm))