import random
import time
totp = 0
num = random.randrange(1, 11)
print('=+=+=+=+=+=+=+=+=+=+=+=')
print('  JOGO DA ADIVINHAÇÃO  ')
print('=+=+=+=+=+=+=+=+=+=+=+=')
print('Eu pensei em um número, tente adivinhá-lo')
print('Lembre-se o intervalo é entre 1 e 10')
acertou = False
while not acertou:
    adv = int(input('Qual número vc escolhe: '))
    totp += 1
    if adv == num:
        print('Você acertou')
        acertou = True

    else:
        print('Está errado! Tente novamente', end=' ')
        if adv < num:
            print('Eu pensei em um MAIOR')
        else:
            print('Eu pensei em um MENOR')
print('Você teve um total de {} tentativas'.format(totp))
