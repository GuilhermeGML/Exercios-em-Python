pos = 0

for i in range(0, 5):
    n = int(input())
    if n % 2 == 0:
        pos += 1

print(f'{pos} valores pares')
