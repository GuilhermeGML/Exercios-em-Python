i = 0
j = 1

while i <= 2:
    for c in range(0, 3):
        n = j + c
        print(f"I={i:.1f} J={n:.1f}")

    i = i + 0.2
    j = j + 0.2