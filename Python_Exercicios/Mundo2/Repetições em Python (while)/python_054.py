'''
    Crie um programa que leia dois valores e mostre um menu na tela:

[ 1 ] somar

[ 2 ] multiplicar

[ 3 ] maior

[ 4 ] novos números

[ 5 ] sair do programa

Seu programa deverá realizar a operação solicitada em cada caso.
'''
# Ler dois valores
n1 = int(input('Digite um primeiro valor: '))
n2 = int(input('Digite um segundo valor: '))


# Menu de Operaçôes
print('[ 1 ] somar')

print('[ 2 ] multiplicar')

print('[ 3 ] maior')

print('[ 4 ] novos números')

print('[ 5 ] sair do programa')

escolha = int(input('Escolha um número: '))

# Laço while para escolher uma operação
while escolha != 5:
    if escolha == 1:
        print('A soma de {} e {} é igual a {}.'.format(n1, n2, (n1+ n2)))
    elif escolha == 2:
        print('A multiplicação de {} e {} é igual a {}.'.format(n1, n2, (n1*n2)))
    elif escolha == 3:
        if n1 > n2:
            print('O número maior é {}.'.format(n1))
        else:
            print('O número maior é {}.'.format(n2))
    elif escolha == 4:
        n1 = int(input('Digite um primeiro valor: '))
        n2 = int(input('Digite um segundo valor: '))
    escolha = int(input('Escolha um número: '))
    
print('FIM DO PROGRAMA!')

    
