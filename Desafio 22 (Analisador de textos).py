nome = str(input('Digite seu nome completo: '))
esp = nome.strip()
name = nome.split()
print('ANALISANDO SEU NOME')
print('Seu nome em maiúsculo fica assim {}'.format(nome.upper()))
print('Seu nome em minusculo fica asssim {}'.format(nome.lower()))
print('Seu nome tem {} letras'.format(len(esp)))
print('Seu primeiro nome é {} e tem {} letras'.format(name[0], nome.find(' ')))

