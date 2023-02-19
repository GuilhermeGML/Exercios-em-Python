from random import randint
mega = []
lista = []
perg = int(input('Quantos jogos deseja fazer: '))
tot = 1
while tot <= perg:
    cont = 0
    while True:
        num = randint(0, 60)
        if num not in mega:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    mega.append(lista[:])
    lista.clear()
    tot += 1
print('=-' * 30)
for i, l in enumerate(mega):
    print(f'Jogo {1+i}: {l}')