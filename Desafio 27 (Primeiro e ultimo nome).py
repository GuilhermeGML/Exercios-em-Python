nome = str(input('Digite seu nome:')).strip()
name = nome.split()
print('Seu primeiro nome é {}'.format(name[0]))
print('Seu último nome é {}'.format(name[len(name)-1]))