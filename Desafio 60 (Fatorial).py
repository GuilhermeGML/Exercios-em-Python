n = int(input('Digite um número: '))
c = n
f = 1
while c > 0:
    f *= c
    c -= 1
print('O fatorial de {} vale {}'.format(n, f))
