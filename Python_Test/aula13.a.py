# Estrutura de Repetição for

# Dando oi 6 vezes
for c in range(0, 6):
    print('OI!!!')
print('FIM!!!')
print()
# Contar de 1 a 6
for c in range(1, 7):
    print(c)
print('FIM')
print()
# Contagem regressiva a partir de 6
for c in range(6, -1, -1):
    print(c)
print('FIM')

# Contar de 2 em 2
for c in range(0, 7, 2):
    print(c)
print('FIM')
print()

# Fazer uma contagem a partir de um número digitado
n = int(input('Digite um número: '))

for c in range(0, n+1):
    print(c)
print('FIM')
print()

# Ler o inicio, o passo e o fim
i = int(input('Inicio: '))
p = int(input('Passo: '))
f = int(input('Fim: '))
for c in range(i, f+1, p):
    print(c)
print('FIM')
print()

# Ler um número n vezes e fazer a soma
s = 0
for c in range(0, 4):
    n = int(input('Digite um número: '))
    s += n
print('A soma dos valores é {}.'.format(s))