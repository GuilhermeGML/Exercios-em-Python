p1 = int(input('Digite o primeiro termo de uma razão: '))
r = int(input('Digite a razão da progreção: '))
decimo = p1 + (10 - 1) * r
for c in range(p1, decimo + r, r):
    print('{}'. format(c), end=' -> ')
print('ACABOU')