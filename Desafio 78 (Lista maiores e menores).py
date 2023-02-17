num = []
for c in range(0, 5):
    num.append(int(input(f'Digite um número para posição {c}: ')))
print('=-' * 30)
print(f'O maior número digitado é {max(num)} na posição ', end='')
for i, v in enumerate(num):
    if v == max(num):
        print(f'{i} ... ', end='')
print()
print(f'O menor número digitado é {min(num)} na posição ', end ='')
for i, v in enumerate(num):
    if v == min(num):
        print(f'{i} ... ', end='')