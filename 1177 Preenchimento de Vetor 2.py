num = int(input())
j = 0

for i in range(1000):
    print(f"N[{i}] = {j}")
    j += 1
    if j == num:
        j = 0