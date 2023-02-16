pv = sm = pvm = 0
while True:
    print('-'*20)
    print('CADASTRE UMA PESSOA')
    print('-'*20)
    idade = int(input('Idade = '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F] ')).strip().upper()[0]
    if idade >= 18:
        pv += 1
    if sexo == 'M':
        sm += 1
    if sexo == 'F':
        if idade >= 20:
            pvm += 1
    print('-'*20)
    perg = ' '
    while perg not in 'SN':
        -perg = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if perg == 'N':
        break
print(f'Há {pv} pessoas maiores de 18')
print(f'Há {sm} pessoas do sexo masculino')
print(f'Há {pvm} pessoas do sexo feminino e maiores de 20')