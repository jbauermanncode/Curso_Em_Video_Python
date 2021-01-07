'''
    Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
'''
# Ler uma espressão
expr = str(input('Digite a expressão: '))

pilha = []
for simb in expr:
    # Quando encontrar um parenteses aberto
    if simb == '(':
        pilha.append('(')
    # Quando encontrar um parenteses fechado
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')