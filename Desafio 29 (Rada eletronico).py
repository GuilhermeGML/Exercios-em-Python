vel = int(input('Qual é a velocidade do carro: '))
if vel<= 80:
    print('Você está na velocidade permitida.')
else:
    mult = (vel - 80) * 7
    print('MULTADO! Paga {}'.format(mult))