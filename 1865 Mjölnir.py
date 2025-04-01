qtn = int(input())
n = 0
while n < qtn:
    var = (input().split())
    nome = var[0]
    forca = int(var[1])
    if nome == 'Thor' and forca > 0:
        print(f'Y')
    else:
        print(f'N')
    n += 1
