'''
    Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
'''
# Ler uma frase
frase = str(input('Escreva uma frase: ')).lower().strip()

# Imprimir
print('Quantos As tem na frase? {}'.format(frase.count('a')))

print('Em que posição a letra A aparece a primeira vez? {}'.format(frase.find('a') + 1))

print('Em que posição a letra A aparece por último? {}'.format(frase.rfind('a') + 1))