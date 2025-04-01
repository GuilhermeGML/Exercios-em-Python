i = 1
j = 7

while i <= 9:
    for c in range(1, 4):
        print(f"I={i} J={j}")
        j = 7
        j = j - c
    i = i + 2
    j = 7