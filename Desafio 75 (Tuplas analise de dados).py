num = (int(input('Digite um número: ')),
       int(input('Digite outro número: ')),
       int(input('Digite o terceiro número: ')),
       int(input('Digite o quarto número: ')))
print(f'Os números digitados foram {num}')
if 9 in num:
    print(f'O valor 9 apareceu {num.count(9)}')
else:
    print('O valor 9 não foi digitado')
if 3 in num:
    print(f'O valor 3 apareceu na {num.index(3)+1} posição')
else:
    print(f'O valor 3 não foi digitado')
print(f'Os números pares digitados foram ', end='')
for c in num:
    if c % 2 == 0:
        print(c, end=' ')
