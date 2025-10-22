a,b,c = list(map(float,input().split()))

if a + b > c and a + c > b and b + c > a:
    per = a + b + c
    print(f"Perimetro = {per:.1f}")
else:
    area = ((a + b) * c)/2
    print(f"Area = {area:.1f}")