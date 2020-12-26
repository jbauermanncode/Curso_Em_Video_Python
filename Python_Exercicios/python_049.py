'''
    Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:

APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.
'''
# Ler frase
frase = str(input('Escreva uma frase: ')).strip().upper()
print('\nVocê digitou a frase: {}'.format(frase))

# Separar a frase por palavras
palavras = frase.split()

# Juntar as palavras sem espaço
junto = ''.join(palavras)

# Iverter as palavras
inverso = ''

# Laço for para inverter a frase
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print('O inverso de {} é {}.'.format(junto, inverso))
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('Não temos um palíndromo!')



