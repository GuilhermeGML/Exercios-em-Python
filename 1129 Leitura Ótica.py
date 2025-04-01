while True:
    qtn = int(input())
    if qtn == 0:
        break
    n = 0
    while n < qtn:
        var = list(map(int, input().split()))
        pos = -1  # Define posição inválida como padrão
        tot = 0
        for i in range(len(var)):
            if var[i] < 127 and var[i] <= 255:
                pos = i
                tot += 1
        if tot > 1 or tot == 0:
            print('*')
        else:
            if pos == 0:
                print('A')
            elif pos == 1:
                print('B')
            elif pos == 2:
                print('C')
            elif pos == 3:
                print('D')
            elif pos == 4:
                print('E')
        n += 1
