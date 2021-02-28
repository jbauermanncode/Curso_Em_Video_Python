'''
    Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.
'''
lista = list()

# Fazer um laço for para o usuario digitar 5 números
for c in range(0, 5):
    n = int(input('Digite um numero: '))
    # Se for o primeiro ou maior que o ultimo numero digitado
    if c == 0 or n > lista[len(lista)-1]:
        lista.append(n)
        print('Adicionado ao final da lista...')
    else:
        # percorrer todas as posições e encontrar a ordem certa para colocar o Número
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na posição {pos} da lista...')
                break
            pos += 1
print('-='*30)
print('Os números digitados são {lista}')
    


    

