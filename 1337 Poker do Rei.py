while True:
    var = list(map(int, input().split()))
    res = 0
    if var[0] == var[1] == var[2] == 0:
        break
    elif var[0] == var[1] == var[2]:
        res = 1 #SET
    elif var[0] == var[1] != var[2]:
        res = 201 #PAR
    elif var[0] != var[1] == var[2]:
        res = 212 #PAR
    elif var[0] == var[2] != var[1]:
        res = 202 #PAR
    else:
        res = 3 #NÃO PAR

    #SET
    if res == 1:
        if var[0] == 13:
            print('*')
        else:
            print(f'{var[0] + 1} {var[1] + 1} {var[2] + 1}')
    #PAR 0 e 1
    elif res == 201:
        if var[0] == 13:
            print(f'{1} {1} {1}')
        elif var[2] == 13:
            print(f'{1} {var[0] + 1} {var[1] + 1}')
        else:
            print(f'{var[0]} {var[1]} {var[2] + 1}')
    #PAR 1 e 2
    elif res == 212:
        if var[1] == 13:
            print(f'{1} {1} {1}')
        elif var[0] == 13:
            print(f'{1} {var[1] + 1} {var[2] + 1}')
        else:
            print(f'{var[0] + 1} {var[1]} {var[2]}')
    #PAR 0 e 2
    elif res == 202:
        if var[0] == 13:
            print(f'{1} {1} {1}')
        elif var[1] == 13:
            print(f'{1} {var[0] + 1} {var[2] + 1}')
        else:
            print(f'{var[1] + 1} {var[0]} {var[2]}')
    # NAO PAR
    elif res == 3:
        print(f'{1} {1} {2}')