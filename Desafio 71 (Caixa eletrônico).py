dinheiro = int(input('Qual valor deseja retirar? '))
while True:

    if dinheiro / 50:
        totced = dinheiro // 50
        dinheiro -= totced * 50
        if totced > 0:
            print(f'Você receberá {totced} notas de 50')
        if dinheiro / 20:
            totced = dinheiro // 20
            dinheiro -= totced * 20
            if totced > 0:
                print(f'Você receberá {totced} notas de 20')
            if dinheiro / 10:
                totced = dinheiro // 10
                dinheiro -= totced * 10
                if totced > 0:
                    print(f'Você receberá {totced} notas de 10')
                if dinheiro / 1:
                    totced = dinheiro // 1
                    dinheiro -= totced * 1
                    if totced > 0:
                        print(f'Você receberá {totced} notas de 1')
    break


#dinheiro = int(input('Qual valor deseja retirar? '))
#total = dinheiro
#ced = 50
#totced = 0
#while True:
#    if total >= ced:
#        total -= ced
#        totced += 1
#    else:
#        if totced > 0:
#        print(f'Total de {totced} cedulas de R$ {ced}')
#        if ced == 50:
#            ced = 20
#        elif ced == 20:
#            ced = 10
#        elif ced == 10:
#           ced = 1
#        totced = 0
#        if total == 0:
#            break