'''
     Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
'''
# Leia um número Inteiro
n = int(input('Digite um número Inteiro: '))

print('A tabuada do número {} é: '.format(n))

# Laço for para fazer a tabuada
for t in range(1, 11):
    m = n * t 
    print('{} x {} = {}'.format(t, n, m))
    print('--'*10)
print('FIM')  
