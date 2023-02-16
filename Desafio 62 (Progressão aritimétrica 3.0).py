p1 = int(input('Digite o primeiro termo de uma razão: '))
r = int(input('Digite a razão da progreção: '))
termo = p1
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print('{} -> '.format(termo), end='')
        termo += r
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais: '))
print('PROGRESSÃO TERMINADA COM {} TERMOS'.format(total))
