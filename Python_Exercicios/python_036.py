'''
    Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
'''
# Ler os valores da casa e do salário
valor_casa = float(input('Qual o valor da casa? R$'))

salario = float(input('Qual o valor do seu salário? R$'))

tempo_de_pagamento = int(input('Em quantos anos pretende pagar? '))

# Calcular o valor da parcela
parcela = (valor_casa / tempo_de_pagamento) / 12

# Calcular o percentual do salario
percentual_salario = int((parcela * 100) / salario)

# Uso de operações Relacionais
emprestimo_autorizado = percentual_salario < 30

emprestimo_autorizado_limite = percentual_salario == 30

print('$$'*40)
print()

# Estrutua Condicional if, elif e else
if emprestimo_autorizado:
    print('PARABÉNS! O seu empréstimo foi autorizado com sucesso.')
    print('A sua parcela por mês será de {:.2f}, o pagamento será concluido em {} anos.'.format(parcela, tempo_de_pagamento))

elif emprestimo_autorizado_limite:
    print('PARABÉNS! O seu empréstimo foi autorizado, mas cuidado pois está no limite de 30% do seu salário.')
    print('A sua parcela por mês será de {:.2f}, o pagamento será concluido em {} anos.'.format(parcela, tempo_de_pagamento))

else:
    print('O seu empréstimo foi negado, pois o valor da parcela ultrapassa 30% do seu salário.')
print()
print('$$'*40)
