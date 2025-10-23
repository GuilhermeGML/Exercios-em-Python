renda = float(input())

if renda <= 2000:
    print('Isento')
elif 2000.01 <= renda <= 3000:
    rendan = renda - 2000
    imp = rendan * 0.08
    print(f'R$ {imp:.2f}')
elif 3000.01 <= renda <= 4500:
    rendan = renda - 3000
    imp = (rendan * 0.18) + 80
    print(f'R$ {imp:.2f}')
elif renda >= 4500.01:
    rendan = renda - 4500
    imp = (rendan * 0.28) + 350
    print(f'R$ {imp:.2f}')
