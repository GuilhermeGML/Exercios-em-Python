num = list()
while True:
    n = int(input('Digite um número: '))
    if n not in num:
        num.append(n)
        print('Número adicionado a lista')
    else:
        print('Número repitido. Desconsiderando ...')
    perg = str(input('Deseja continuar: [S/N] ')).strip().upper()[0]
    if perg == 'N':
        break
sorted(num)
print(num)
