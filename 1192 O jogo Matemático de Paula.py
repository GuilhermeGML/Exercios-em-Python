n = int(input())
for i in range(n):
    entrada = input()
    n1 = int(entrada[0])
    l = entrada[1]
    n2 = int(entrada[2])
    if n2 == n1:
        tot = n1 * n2
    elif l == str.upper(l):
        tot = n2 - n1
    elif l == str.lower(l):
        tot = n2 + n1

    print(f'{tot}')
    i += 1