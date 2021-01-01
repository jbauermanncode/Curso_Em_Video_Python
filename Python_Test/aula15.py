n = s = 0
while True:
    n = int(input('Digite um numero: '))
    if n == 999:
        break
    s += n
# Usando f string para formatar o print    
print(f'A soma vale {s:.2f}.')
