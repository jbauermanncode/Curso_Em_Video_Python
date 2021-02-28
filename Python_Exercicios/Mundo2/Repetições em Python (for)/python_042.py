'''
    Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.
'''
# Importar sleep que conta um segundo 
from time import sleep

# Laço for para contagem regressiva
for i in range(10, 0, -1):
    print(i)
    sleep(1)
    print()
print('**'*10)
print()
print('FELIZ ANO NOVO!!!!')
print()
print('**'*10)