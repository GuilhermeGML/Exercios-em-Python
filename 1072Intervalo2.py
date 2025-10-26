n=int(input())

den = 0
fora = 0
for i in range (0, n):
    num = int(input())
    if 10 <= num <= 20:
        den += 1
    else:
        fora += 1

print(f"{den} in")
print(f"{fora} in")