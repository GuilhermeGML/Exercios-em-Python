segundo = int(input())
hora = 0
min = 0

if segundo >= 3600:
    while segundo >= 3600:
        segundo -=3600
        hora += 1

if segundo >= 60:
    while segundo >= 60:
        segundo -=60
        min += 1

print(f"{hora}:{min}:{segundo}")