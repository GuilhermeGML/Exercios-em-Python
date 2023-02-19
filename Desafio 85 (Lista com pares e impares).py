num = [[], []]
for c in range(0, 7):
    valor = int(input(f'Digite um valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
print('-=' * 30)
num[0].sort()
num[1].sort()
print(f'Os valores pares digitedos foram {num[0]}')
print(f'Os valores impares digitedos foram {num[1]}')