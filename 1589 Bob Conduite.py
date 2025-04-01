qtn = int(input())
n=0
while n<qtn:
    var = list(map(int, input().split()))

    r1 = var[0]
    r2 = var[1]

    rt = r1 +r2
    print(f'{rt}')
    n += 1


