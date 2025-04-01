import math

a, b, c = input().split(" ")
a = float(a)
b = float(b)
c = float(c)

x = b*b - 4*a*c

if a == 0 or x < 0:
    print("Impossivel calcular")
else:
    raiz1 = (-b + math.sqrt(x)) / (2 * a)
    raiz2 = (-b - math.sqrt(x)) / (2 * a)
    print(f"R1 = {raiz1:.5f}")
    print(f"R2 = {raiz2:.5f}")