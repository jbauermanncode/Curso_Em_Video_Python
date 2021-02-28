'''
    Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250.00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
'''
# Ler salário
salario = float(input('Informe o salário: R$'))

print('O atual salário é de R${:.2f}.'.format(salario))

# Estrutura Condicional if/else
if salario > 1250.00:
    novo = salario + (salario * (10 / 100))
else:
    novo = salario + (salario * (15 / 100))

print('O salário passará para R${:.2f}.'.format(novo))
