from random import randint
import time
from operator import itemgetter
jogo = dict()
jogo['jogador1'] = randint(1, 6)
jogo['jogador2'] = randint(1, 6)
jogo['jogador3'] = randint(1, 6)
jogo['jogador4'] = randint(1, 6)
rank = {}
print('JOGO DE DADOS')
for k, v in jogo.items():
    print(f'O {k} tirou {v}')
    time.sleep(2)
rank = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('=-' * 20)
print('RANKING DOS JOGADORES')
for i, v in enumerate(rank):
    print(f'{1 + i} lugar: {v[0]} com {v[1]}')
    time.sleep(2)