for c in range(1, 10):
    print(c)
print('FIM')

w = 1
while w < 10:
    print(w)
    w = w +1
print('FIM')

for i in range(1, 5):
    n = int(input('Digite um número: '))
print('FIM')

num = 1
while num != 0:
    num = int(input('Digite um número: '))
print('FIM')

r = 'S'
while r == 'S':
    number = int(input('Digite um número: '))
    r = str(input('Continuar? [S/N]: ')).upper()
print('FIM')

numero = 1
par = impar = 0
while numero != 0:
    numero = int(input('Digite um número: '))
    if numero != 0:
        if numero % 2 == 0:
            par +=1
        else:
            impar += 1
print('Você digitou {} números pares, e {} números ímpares.'.format(par, impar))

