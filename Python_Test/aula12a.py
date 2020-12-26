nome = str(input('Qual o seu nome: '))

if nome == 'Josué':
    print('Que nome bonito!')

elif nome == 'Rosicléia' or nome=='Astolfo':
    print('Que nome feio!')

elif nome == 'Maria' or nome == 'João' or nome == 'Pedro' or nome == 'Ana':
    print('Seu nome é bem popular!')

elif nome == 'Kevin' or nome == 'Kelly' or nome == 'Cristhian':
    print('Seu nome tem origem estrangeira!')
elif nome in ('Fernanda Bianca Beatriz Jaqueline'):
    print('Que belo nome feminino você tem!')

else:
    print('Seu nome é bem normal!'.format(nome))

print('Tenha um bom dia, {}!'.format(nome))