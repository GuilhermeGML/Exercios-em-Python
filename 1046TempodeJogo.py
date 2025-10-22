a, b = list(map(int,input().split()))

if b > a:
    temp = b - a
    print(f"O JOGO DUROU {temp} HORA(S)")
elif a > b:
    temp = (24 - a) + b
    print(f"O JOGO DUROU {temp} HORA(S)")
elif a == b:
    print(f"O JOGO DUROU 24 HORA(S)")