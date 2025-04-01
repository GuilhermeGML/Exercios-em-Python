while True:
    aprov = 0
    while aprov != 1:
        p1 = float(input())
        if p1 < 0 or p1 > 10:
            print("nota invalida")
        else:
            aprov = 1
    aprov = 0
    while aprov != 1:
        p2 = float(input())
        if p2 < 0 or p2 > 10:
            print("nota invalida")
        else:
            aprov = 1

    media = (p1 + p2) / 2
    break

print(f"media = {media:.2f}")
