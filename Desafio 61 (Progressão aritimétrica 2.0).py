p1 = int(input('Digite o primeiro termo de uma razão: '))
r = int(input('Digite a razão da progreção: '))
dec = 1
x = 1
print('{} -> '.format(p1), end='')
while dec < 10:
    dec += 1
    x = p1 + (dec - 1) * r
    print('{} -> '.format(x), end='')
print('FIM')
