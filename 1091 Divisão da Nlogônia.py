while True:
    qnt = int(input())
    n = 0
    var = list(map(int, input().split()))
    x1 = var[0]
    y1 = var[1]
    while n < qnt:
        var = list(map(int, input().split()))
        x = var[0]
        y = var[1]
        if x == x1 or y == y1:
            print(f'divisa')
        else:
            if x > x1 and y > y1:
                print(f'NE')
            elif x < x1 and y > y1:
                print(f'NO')
            elif x < x1 and y < y1:
                print(f'SO')
            elif x > x1 and y < y1:
                print(f'SE')
        n += 1
    if qnt == 0:
        break
