a, b, c, d = input().split(" ")
a = int(a)
b = int(b)
c = int(c)
d = int(d)
test = 0
if b > c and d > a:
    test += 1
if (c+d) > (a+b):
    test += 1
if c > 0 and d > 0:
    test += 1
if a % 2 == 0:
    test += 1

if test == 4:
    print("Valores aceitos")
else:
    print(f"Valores nao aceitos")