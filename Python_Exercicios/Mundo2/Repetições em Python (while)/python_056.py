'''
    Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).
'''
# Iniciar as variaveis
n = s = 0
contador = 0

# Laço while para pedir somar e ver quantos numeros tem
while True:
    n = int(input('Digite um numero: '))
    if n == 999:
        # Quebra do laço while, quando se digita 999
        break
    s += n
    contador += 1
# Usando f string para formatar o print    
print(f'A soma vale {s}.')
print(f'Foram digitados {contador}', end='')
print(' números.' if contador > 1   else ' número.')