dist = float(input('Qual é a distancia em Km da usa viagem? '))
if dist <= 200:
    pag1 = dist * 0.5
    print('Sua viagem custará {} reais'.format(pag1))
else:
    pag2 = dist * 0.45
    print('Sua viagem custará {} reais'.format(pag2))
print('Boa Viagem!')
