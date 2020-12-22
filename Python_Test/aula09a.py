frase = 'Curso em Vídeo Python'
frase2 = '   Aprenda Python  '

print(frase[3])
print(frase[3:13])
print(frase[:13])
print(frase[13:])
print(frase[9:21:2])
print(frase[9::3])
print(frase[::2])
print(len(frase))
print(frase.count('o'))
print(frase.find('deo'))
print(frase.find('Android'))
print('Curso' in frase)
print(frase.replace('Python', 'Android'))
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())
print(frase.split())
print('-'.join(frase))
print(frase.upper().count('O'))

print(frase2.strip())
print(frase2.rstrip())
print(frase2.lstrip())

print('''Python is a programming language that lets you work quickly and integrate systems more effectively.''')