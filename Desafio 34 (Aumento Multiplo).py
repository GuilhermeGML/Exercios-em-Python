sal = float(input('Digite seu salário: '))
if sal > 1250.00:
    nsal = sal * 1.1
    print('Seu novo salário é de {:.3f}'.format(nsal))
else:
    nsal = sal * 1.15
    print('Seu novo salário é de {:.3f}'.format(nsal))