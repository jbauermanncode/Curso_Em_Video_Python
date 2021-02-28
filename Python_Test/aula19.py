pessoas = {'nome': 'Josué', 'sexo': 'M', 'idade': 30}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())

for k in pessoas.keys():# pessoas.items(),pessoas.values()
    print(k)

pessoas['peso'] = 67.5

# Criar um dicionário dentro de uma lista
brasil = list()
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}

brasil.append(estado1)
brasil.append(estado2)

print(brasil[1]['sigla'])

print('-='*30)

# ler dicionarios
estado = dict()
brasil = []

for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())# para fazer uma cópia do dicionário
for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}.')