while True:
    soma = 0
    m, n = map(int, input("").split())
    if m == 0 or n == 0:
        break
    elif m > n:
        for i in range(n, m + 1):
            print(f"{i}", end=" ")
            soma += i
        print(f"Sum={soma}")
        soma = 0
    elif m < n:
        for i in range(m, n + 1):
            print(f"{i}", end=" ")
            soma += i
        print(f"Sum={soma}")
        soma = 0


