'''
    Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo. Informe:

    – EQUILÁTERO: todos os lados iguais

    – ISÓSCELES: dois lados iguais, um diferente

    – ESCALENO: todos os lados diferentes
'''
print('-='*20)
print('Analisador de Triângulos')
print('-='*20)
# Ler 3 retas
r1 = float(input('Informe o valor: '))
r2 = float(input('Informe o valor: '))
r3 = float(input('Informe o valor: '))

# Usando Operadores Relacionais
equilatero = r1 == r2 == r3

isosceles = (r1 == r2 != r3) or (r1 == r3 != r2) or (r2 == r3 != r1)

escaleno = r1 != r2 != r3 != r1


# Estrutura Condicional if, elif, else
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima podem formar um triângulo!', end=' ')

    if equilatero:
        print('EQUILÁTERO!')

    elif isosceles:
        print('ISÓSCELES!')

    elif escaleno:
        print('ESCALENO!')

else:
    print('Os segmentos acima não podem formar um triângulo')