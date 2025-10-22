a, b, c = list(map(int,input().split()))

ord = []
ord.append(a)
ord.append(b)
ord.append(c)

org = []
org.append(ord[0])
org.append(ord[1])
org.append(ord[2])

ord.sort()

for i in range(3):
    print(f'{ord[i]}')

print()
for i in range(3):
    print(f'{org[i]}')