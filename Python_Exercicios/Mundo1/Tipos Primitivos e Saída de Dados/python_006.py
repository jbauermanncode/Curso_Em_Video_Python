'''
Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
'''
# Leia um número inteiro
n = int(input('Digite um valor: '))

# Mostrar o dobro 
d = n * 2

# Mostrar o triplo com outra maneira
t = n * 3

# Mostrar a raiz quadrada
rq = float(n ** (1/2))

print('Qual o dobro, o triplo e a raiz quadrada de {}?'.format(n))
print('{} é o dobro, {} é o triplo e {:.2f} é a raiz quadrada.'.format(d, t, rq))