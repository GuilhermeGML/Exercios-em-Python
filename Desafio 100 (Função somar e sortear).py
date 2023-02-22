# Funções do Programa
from random import randint


def sortear(lista):
    print('Sorteando 5 valores')
    for c in range(0, 5):
        n = randint(0, 10)
        lista.append(n)
        print(f'{n}', end=' ', flush=True)
    print('Pronto!')


def somaPar(lista):
    soma = 0
    for v in lista:
        if v % 2 == 0:
            soma += v
    print(f'Somando os valores pares de {lista}, temos {soma}')


# Programa Principal
números = list()
sortear(números)
somaPar(números)
