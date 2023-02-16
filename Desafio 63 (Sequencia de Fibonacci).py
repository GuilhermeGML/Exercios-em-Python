num = int(input('Digite um número: '))
c = 3
n1 = 0
n2 = 1
print('{} -> {} ->'.format(n1, n2), end=' ')
while c <= num:
    n3 = n1 + n2
    print('{} ->'.format(n3), end=' ')
    n1 = n2
    n2 = n3
    c += 1
print('FIM')
