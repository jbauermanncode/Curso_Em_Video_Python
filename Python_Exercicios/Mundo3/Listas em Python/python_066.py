'''
    Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:                                                                                                                 A) Quantos números foram digitados.                                                                                                              B) A lista de valores, ordenada de forma decrescente.                                                                    
    C) Se o valor 5 foi digitado e está ou não na lista.
'''
# Aplicar uma lista
numeros = list()
contador = 0

# Aplicar um laço while que enquanto for verdadeiro pedir para o usuário digitar um número
while True:
    n = int(input('Digite um número: '))
    numeros.append(n)
    contador += 1
    r = str(input('Deseja continuar? Digite S para continuar ou N para parar: '))

    if r in 'Nn':
        break
    
# Fazer a ordem decrescente
numeros.sort(reverse=True)

print(f'A quantidade de números digitados foi {contador}')
print(f'A ordem descrecente é {numeros}')
# Para saber se o número 5 está na lista
if 5 in numeros:
    print('O número 5 está na lista')
else:
    print('O número 5 não está na lista')
