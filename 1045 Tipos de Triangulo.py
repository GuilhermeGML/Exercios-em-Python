a, b, c = input().split(" ")
a = float(a)
b = float(b)
c = float(c)
maior = 0
if a > maior:
    maior = a
if b > maior:
    maior = b
    b = a
    a = maior
if c > maior:
    maior = c
    c = a
    a = maior

if a >= (b+c):
    print("NAO FORMA TRIANGULO")
elif (a*a) == (b*b) + (c*c):
    print("TRIANGULO RETANGULO")
elif (a*a) > (b*b) + (c*c):
    print("TRIANGULO OBTUSANGULO")
elif (a*a) < (b*b) + (c*c):
    print("TRIANGULO ACUTANGULO")

if a == b == c:
    print("TRIANGULO EQUILATERO")
elif a==b or b==c or c==a:
    print("TRIANGULO ISOSCELES")

