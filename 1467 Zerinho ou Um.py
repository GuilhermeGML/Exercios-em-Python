a, b, c = map(int,(input().split()))

if a == b and a != c:
    print("C")
elif a == c and a != b:
    print("B")
elif b == c and a != c:
    print("A")
elif a == b == c:
    print("*")