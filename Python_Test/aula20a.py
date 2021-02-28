def soma(a, b):
    print(f'A = {a} e B = {b}.')
    s = a + b
    print(f'A soma de A + B = {s}.')

# Programa Principal
soma(a=4, b=5)
soma(b=8, a=9)
soma(2, 1)

# Empacotamento
def contador(* num):
    for valor in num:
        print(f'{valor} ', end=' ')
    print('FIM!')   
    tam = len(num)
    print(f'O total de números é {tam}!')

contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)

# Trabalhando com listas
def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1

valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)

# Desempacotamento
def soma(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')

soma(5, 2)
soma(2, 9, 4)