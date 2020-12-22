# Ler duas notas
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

# Calcular a média das notas
m = (n1 + n2) / 2

# Imprimir a média
print('A sua média foi {:.1f}.'.format(m))

# Analisar a condição da média
if m >= 6.0:
    print('Sua média foi boa! PARABÉNS')
else:
    print('Sua média foi ruim! ESTUDE MAIS!')

