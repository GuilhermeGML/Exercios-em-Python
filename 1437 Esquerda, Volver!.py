while True:
    n = int(input())
    if n == 0:
        break
    totd = 0
    tote = 0
    tot = 0
    res = input().upper()
    for i in range(n):
        if res[i] == "D":
            totd += 1
        elif res[i] == "E":
            tote += 1

    if totd > tote:
        tot = totd - tote
    elif tote > totd:
        tot = tote - totd

    if tot == 0:
        print("N")
    elif tot == 1 and totd > tote:
        print("L")
    elif tot == 1 and tote > totd:
        print("O")
    elif tot == 2:
        print("S")
    elif tot == 3 and totd > tote:
        print("L")
    elif tot == 3 and tote > totd:
        print("O")