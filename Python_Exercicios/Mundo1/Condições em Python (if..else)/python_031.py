'''
    Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km, e R$0,45 para viagens mais longas.
'''
# Ler Distância
distancia = int(input('Informe a distância que será percorrida: '))
print('A distância é de {}Km.'.format(distancia))
print('--'* 30)

# Estrutura Condicional if/else.
if distancia <= 200:
    print('O custo da passagem é de R${:.2f}.'.format(distancia * 0.50)) 
else:
    print('O custo da passagem é de R${:.2f}.'.format(distancia * 0.45))