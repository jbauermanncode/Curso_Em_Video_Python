'''
    Crie um programa que tenha uma Tupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
'''
# Tupla com números por extenso
extenso = ('Zero','Um','Dois','Três','Quatro','Cinco','Seis','Sete','Oito','Nove','Dez','Onze','Doze','Treze','Quatorze','Quinze','Dezesseis','Dezessete','Dezoito','Dezenove','Vinte')

# Ler um número e imprimir ele por extenso
while True:
    n = int(input('Digite um número de 0 à 20: '))
    if 0 <= n <= 20:
        break
    print('Tente novamente.', end= '\n')
print(f'Você digitou {extenso[n]}.')