'''
    Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.
'''
# Aplicar uma lista
numeros = []
pares = []
impares =[]

# Aplicar um laço while que enquanto for verdadeiro pedir para o usuário digitar um número
while True:
    numeros.append(int(input('Digite um número: ')))
    
    r = str(input('Deseja continuar? Digite S para continuar ou N para parar: '))
    if r in 'Nn':
        break
# para saber se o numero é par ou impar
for i, v in enumerate(numeros):
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)
print(f'A lista original tem os valores {numeros}!')
print(f'A lista de pares tem os valores {pares}')
print(f'A lista de impares tem os valores {impares}')