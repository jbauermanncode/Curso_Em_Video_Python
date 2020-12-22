'''
    Escreva um programa que converta uma temperatura digitada em Celsius para Farenheit.
'''
# Ler Temperatura
c = float(input('Informe a temperatura em °C: '))

# Converter para °F
f = ((9 * c) / 5) + 32

# Imprimir na tela
print('A temperatura de {}°C corresponde a {}°F!'.format(c, f))
