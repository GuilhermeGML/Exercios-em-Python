import random
import time

num = random.randrange(1, 6)
print('=+=+=+=+=+=+=+=+=+=+=+=')
print('  JOGO DA ADIVINHAÇÃO  ')
print('=+=+=+=+=+=+=+=+=+=+=+=')
print('Eu pensei em um número, tente adivinhá-lo')
print('Lembre-se o intervalo é entre 1 e 5')
adv = int(input('Qual número vc escolhe: '))
print('PROCESSANDO')
time.sleep(3)
if adv==num:
    print('Parabens! Você acertou!')
else:
    print('Você errou! Eu pensei no {}'.format(num))