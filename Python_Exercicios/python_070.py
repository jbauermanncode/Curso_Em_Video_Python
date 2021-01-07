'''
    Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.
'''
# Declarar duas listas internas
num = [[], []]

# Variaveis
valores = 0

# Fazer um laço for com um contador
for c in range(1, 8):
    valor = int(input(f'Digite o {c}o. valor: '))
    # Para colocar o valor na posição de par
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
print('-=' * 30)

# Para colocar em ordem crescente
num[0].sort()
num[1].sort()

print(f'Todos os valores: {num}!')
# Imprimir só os valores pares
print(f'Os valores pares são {num[0]}')
# Imprimir só os valores impares
print(f'Os valores pares são {num[1]}')