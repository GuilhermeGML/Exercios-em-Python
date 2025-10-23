pos = 0
med = 0

for i in range(0, 6):
    n = float(input())
    if n > 0:
        pos += 1
        med += n


print(f'{pos} valores positivos')
print(f'{med/pos:.1f}')

