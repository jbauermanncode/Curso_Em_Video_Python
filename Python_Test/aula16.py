lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
print(lanche[0:4])
print()
print('-++'*20)
print()

# Usando laço for
for cont in range(0, len(lanche)):
    print(lanche[cont])
print()
print('-++'*20)
print()

for comida in lanche:
    print(f'Eu vou comer {comida}.')
print()
print('-++'*20)
print()


# Para saber a posição
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}.')
print()
print('-++'*20)
print()

# Para saber a posição usando enumerate
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}.')
print()
print('-++'*20)
print()

# Mostrar o lanche em ordem
print(sorted(list(lanche)))
print()
print('-++'*20)
print()

print('Comi pra caramba!')
print()
print('-++'*20)
print()


a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a
print(c)
print(c.index(4))
print()
print('-++'*20)
print()

pessoa = ('Gustavo', 39, 'M', 99.88)
print(pessoa)