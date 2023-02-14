tpu = 0
tpd = 0
for c in range(1, 6):
    peso = float(input('Pedo da {} pessoa: '.format(c)))
    if peso > tpu:
        tpu = peso
    else:
        tpd = peso
print('O maior peso é {}'. format(tpu))
print('O menor peso é {}'.format(tpd))