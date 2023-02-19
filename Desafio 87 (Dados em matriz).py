matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
par = list()
spar = mai = scol = slin = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um núemro para posiçõa {l+1} {c+1}:'))
print('=' * 25)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c]
        elif matriz[l][c] >= 0:
            if matriz[l][c] > mai:
                mai = matriz[l][c]
    if c == 2:
        scol += matriz[l][2]

    print()
print('=' * 25)
print(f'A soma dos números pares digitados são {spar}')
print(f'A soma dos valores da terceira coluna é {scol}')
print(f'o maior valor digitado é {mai}')
