def area(a, b):
    s = a * b
    print(f'A área de um terreno de largura {a} x {b} é de {s}')


print('CONTROLE DE TERRENOS')
l = float(input('LARGURA = '))
c = float(input('COMPRIMENTO = '))
area(l, c)
