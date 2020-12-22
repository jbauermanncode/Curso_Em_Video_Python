'''
    Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
'''
# Ler o preço de um produto
preco = float(input('Qual é o preço do produto? R$ '))

# novo preço com desconto
novo = preco - (preco * 5 / 100)

# Imprimir na tela
print('O preço que custava R${}, na promoção vai custar R${}.'.format(preco, novo))