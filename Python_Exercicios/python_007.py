'''
   Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
'''
# Ler notas
n1 = float(input('Digite uma nota: '))
n2 = float(input('Digite outra nota: '))

# Calcular média
m = float((n1 + n2)/2)

# Imprimir média
print('Nota da Prova: {:.1f}'.format(n1))
print('Nota do Trabalho: {:.1f}'.format(n2))
print('------------------------------------')
print('Média: {:.1f}'.format(m))