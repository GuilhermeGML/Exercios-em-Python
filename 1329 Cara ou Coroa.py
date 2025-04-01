while True:
    n = int(input())
    if n == 0:
        break
    m = 0
    j = 0
    for i in range(n):
        var = int(input())
        if var == 1:
            j += 1
        elif var == 0:
            m += 1

    print(f'Mary won {m} times and John won {j} times')