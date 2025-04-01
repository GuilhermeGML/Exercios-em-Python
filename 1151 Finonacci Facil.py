fibo=[0,1]
p=0
s=1
num = int(input())
for i in range(num):
    t=s+p
    fibo.append(t)
    p=s
    s=t
    print(f"{fibo[i]}", end=" ")
