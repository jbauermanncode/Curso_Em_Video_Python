'''
    Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostra quantos Dólares ela pode comprar.
'''

# Leia o valor que tem na carteira
r = float(input('Digite quanto de dinheiro você possui na carteira: '))

# Transformar para dólar
d = float(r / 3.27)

# Imprimir na Tela
print('Tem {:.2f}R$ na carteira'.format(r))
print('Isso equivale a {:.2f}$ dólares.'.format(d))
