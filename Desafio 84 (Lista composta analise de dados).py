pessoas = []
galera = []
totpeso = []
totleve = []
totp = 0
print('=-' * 30)
print('As pessoas mais pesadas serão consideradas acima de 80 Kg')
print('=-' * 30)
while True:
    pessoas.append(str(input('Nome: ')))
    pessoas.append(float(input('Peso: ')))
    galera.append(pessoas[:])
    pessoas.clear()
    perg = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    totp += 1
    if perg in 'N':
        break
for p in galera:
    if p[1] >= 80:
        totpeso.append(p[0])
    elif p[1] < 80:
        totleve.append(p[0])
print(f'Foram cadastradas {totp} pessoas')
print(f'As pessoas mais pesadas são {totpeso}')
print(f'As pessoas mais pesadas são {totleve}')