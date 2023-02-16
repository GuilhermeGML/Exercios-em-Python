tot = totm = menor = c = 0
barato = ''
while True:
    print('-='*20)
    print('LOJA GENIUS')
    print('-=' * 20)
    produto = str(input('Nome: '))
    preço = float(input('Preço R$:'))
    tot += + preço
    if preço > 1000:
        totm += 1
    if c == 0:
        menor = preço
        barato = produto
    else:
        if preço < menor:
            menor = preço
            barato = produto
    perg = ' '
    while perg not in 'SN':
        perg = str(input('Deseja continuar? [S/N] :')).strip().upper()[0]
    if perg == 'N':
        break
print(f'O total gasto foi de {tot}')
print(f'Há {totm} produtos que custam mais de 1000 reais')
print(f'O produto mais barato foi {barato}')