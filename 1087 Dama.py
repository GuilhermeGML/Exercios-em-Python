while True:
    var = list(map(int, input().split()))
    x1, y1, x2, y2 = var[0], var[1], var[2], var[3]
    if x1 == x2 == y1 == y2 == 0:
        break

    if x1 == x2 and y1 == y2:
        print('0')
    elif x1 == x2 or y1 == y2:
        print('1')
    elif abs(x1 - x2) == abs(y1 - y2):
        print('1')
    else:
        print('2')
