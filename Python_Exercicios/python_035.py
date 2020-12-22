'''
    Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
'''
print('-='*20)
print('Analisador de Triângulos')
print('-='*20)
# Ler 3 retas
r1 = float(input('Informe o valor: '))
r2 = float(input('Informe o valor: '))
r3 = float(input('Informe o valor: '))

# Estrutura Condicional if/else
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima podem formar um triângulo!')
else:
    print('Os segmentos acima não podem formar um triângulo')

