a = float(input('Digite um número: '))
b = float(input('Digite outro número: '))
c = float(input('Digite mais um número: '))
maior = 0
menor = 0
if a > b and a > c:
    maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O maior número é {}'.format(maior))

if a < b and a < c:
    menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
print('O menor núemro é {}'.format(menor))
