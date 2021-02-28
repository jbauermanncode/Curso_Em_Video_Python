'''
    Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
'''
numeros = list()

# Ler valores enquanto o usuario responder S
while True:
    n = int(input('Digite um número: '))

    # Quando o numero digitado não for repetido
    if n not in numeros:
        numeros.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    r = str(input('Quer continuar? Sim ou Não S/N: '))

    # Para quebrar a sequencia do laço while
    if r in 'nN':
        break
print('-='*30)
numeros.sort()
print(f'Você digitou os valores {numeros}!')

    
        
     
        
   



            
