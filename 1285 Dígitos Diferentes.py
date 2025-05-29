n, m = map(int,(input().split()))
tot = 0

while n <= m:
    un = n // 1 % 10
    dn = n // 10 % 10
    cn = n // 100 % 10
    mn = n // 1000 % 10
    if n < 100:
        if un != dn:
            tot += 1
    elif 100 <= n < 1000:
        if un != dn and un != cn and dn != cn:
            tot += 1
    elif 1000 <= n <= 5000:
        if un != dn and un != cn and un != mn and dn != cn and dn != mn and cn != mn:
            tot += 1
    n += 1


print(tot)
