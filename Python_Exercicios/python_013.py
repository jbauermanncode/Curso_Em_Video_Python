'''
    Faça um algoritmo que leia o salario de um funcionário e mostre seu novo salário, com 15% de aumento.
'''
# Leia Salário
salario = float(input('Qual é o salário do funcionário? R$'))

# Calcular novo Salário
novo = salario + (salario * 15 / 100)

# Imprimir na tela
print('Um funcionário que ganhava R${:.2f}, com 15% de aumento, passou a receber R${:.2f}'.format(salario, novo))
