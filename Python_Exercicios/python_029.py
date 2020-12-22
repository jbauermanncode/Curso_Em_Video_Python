'''
    Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
'''
# Ler a velocidade do carro.
vc = int(input('Informe a velocidade do carro: '))


print('--*-'* 20)
print('A velocidade registrada é de {}Km/h.'.format(vc))
print('--*-'* 20)

# Estrutura Condicional if/else
if vc > 80:
    print('Você foi MULTADO! Pois excedeu o limite de 80Km/h. E agora deve R${:.2f} reais.'.format((vc - 80) * 7))
else:
    print('PARABÉNS!!!!')
print('--$-'* 20)


