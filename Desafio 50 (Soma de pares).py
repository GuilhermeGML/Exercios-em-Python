s = 0
cont = 0
for c in range(1, 7):
     num = int(input('Digite um número = '))
     if num % 2 == 0:
        s += num
        cont += 1
print('Teve {} numeros pares e a soma deles é {}'.format(cont, s))
