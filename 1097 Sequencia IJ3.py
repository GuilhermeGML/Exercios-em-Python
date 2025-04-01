i = 1
j = 7

while i <= 9:
    for c in range(0, 3):
        n = j - c
        print(f"I={i} J={n}")
        n = j
    i = i + 2
    j = j + 2
