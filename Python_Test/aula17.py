print('Lista 1')
num = [2, 5, 9, 1]
print(num)
print('*'*40)

print('Lista 2')
num[2] = 3
num.append(7)
print(num)
num.sort()
print(num)
print('*'*40)

print('Lista 3')
num.sort(reverse=True)
print(num)
num.insert(2, 0)
print(num)
print(f'Essa lista tem {len(num)} elementos.')
print('*'*40)

print('Lista 4')
num.pop()
num.pop(2)
print(num)
num.insert(2, 2)
print(num)
num.remove(2)
print(num)
if 4 in num:
    num.remove(4)
    print(num)
else:
    print('Esse elemento não existe na lista.')
print('*'*60)
print()

valores = []
valores.append(5)
valores.append(9)
valores.append(4)

for v in valores:
    print(f'{v}...', end=' ')

# Para pegar os valores e a posição deles
for c, v in enumerate(valores):
    print(f'\nNa posição {c} encontra- se o valor {v}!')
print('Cheguei ao final da lista.')
print('*'*60)
print()

print('Lista 5')
# Ler valores pelo teclado e adicionar a lista
valores = list()
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
for c, v in enumerate(valores):
    print(f'Na posição {c} encontra- se o valor {v}!')
print('Cheguei ao final da lista.')
print('*'*60)
print()

print('Lista 6')
a = [2, 3, 4, 7]
print(a)
# Para b fazer uma cópia de a
b = a[:]
# Para b igualar a a
#b = a
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')



