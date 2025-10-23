pos = 0
neg = 0
par = 0
imp = 0

for i in range(0, 5):
    n = int(input())
    if n % 2 == 0:
        par += 1
    elif n % 2 == 1:
        imp += 1
    
    if n > 0:
        pos += 1
    elif n < 0:
        neg += 1

print(f'{par} valor(es) par(es)')
print(f'{imp} valor(es) impar(es)')
print(f'{pos} valor(es) positivo(s)')
print(f'{neg} valor(es) negativo(s)')
