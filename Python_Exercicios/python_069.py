'''
    Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:                                                                                                    
A) Quantaspessoasforamcadastradas.                                                                                       B) Uma listagem com as pessoas mais pesadas.                                                                                                    
C) Uma listagem com as pessoas mais leves.
'''
pessoas = list()
inf = list()
cont = 0
maior = menor = 0

# Fazer um laço while para ler nome de varias pessoas e colocar uma lista dentro da outra
while True:
    inf.append(str(input('Nome: ')))
    cont += 1
    inf.append(int(input('Peso: ')))
    # Para saber as pessoas mais pesadas e mais leves
    if len(pessoas) == 0:
        maior = menor = inf[1]
    else:
        if inf[1] > maior:
            maior = inf[1]
        if inf[1] < menor:
            menor = inf[1]
    # Adicionar a lista inf na lista pessoas
    pessoas.append(inf[:])
    # Limpar depois de cadastrar
    inf.clear()
    # Pedir se quer continuar ou Não
    resp = str(input('Deseja continuar? Se sim digite S, se não digite N: '))
    if resp in 'nN':
        break
print('-='*30)
print()
print(f'Os dados cadastrados foram {pessoas}.')
# Pode usar um contador ou um len da lista pessoas
print(f'Ao todo você cadastrou {cont} pessoas.')
print(f'Ao todo você cadastrou {len(pessoas)} pessoas.', )
#-------------------------------------------------

# Descobrindo quais são as pessoas mais leves e pesadas
print(f'O maior peso foi de {maior}kg.', end= ' ')
for p in pessoas:
    if p[1] == maior:
        print(f'[{p[0]}]', end='')
print()

print(f'O menor peso foi de {menor}kg.', end= ' ')
for p in pessoas:
    if p[1] == menor:
         print(f'[{p[0]}]', end='')
print()