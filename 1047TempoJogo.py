h1, m1, h2, m2 = list(map(int, input().split()))

if h2 > h1 and m2 > m1:
    toth = h2 - h1
    totm = m2 - m1

elif h2 > h1 and m1 > m2:
    toth = (h2 - h1) - 1
    totm = 60 - (m1 - m2)

elif h1 > h2 and m1 > m2:
    toth = 24 - (h1 - h2) - 1
    totm = 60 - (m1 - m2)

elif h1 > h2 and m2 > m1:
    toth = 24 - (h1 - h2)
    totm = m2 - m1

elif h1 == h2 and m1 > m2:
    toth = 23
    totm = 60 - (m1 - m2)

elif h1 == h2 and m2 > m1:
    toth = 0
    totm = m2 - m1

elif h1 > h2 and m1 == m2:
    toth = 24 - (h1 - h2)
    totm = 0

elif h2 > h1 and m2 == m1:
    toth = h2 - h1
    totm = 0

elif h1 == h2 and m1 == m2:
    toth = 24
    totm = 0

print(f"O JOGO DUROU {toth} HORA(S) E {totm} MINUTO(S)")
