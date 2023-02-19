num = []

while True:
    num.append(int(input('Digite um núemro: ')))
    perg = str(input('Digite um núemro: [S/N] ')).strip().upper()[0]
    if perg in 'N':
        break
print(f'Houve {len(num)} números digitados')
num.sort(reverse=True)
print(f'A ordem invertida é {num}')
if 5 in num:
    print('Os valor 5 faz parte da lista')
else:
    print('Os valor 5 não faz parte da lista')