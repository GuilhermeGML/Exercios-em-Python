from datetime import date
atual = date.today().year
tota = 0
tote = 0
for c in range(1, 8):
    idade = int(input('Digite o ano em que você nasceu: '))
    if atual - idade >= 18:
        tota += 1
    else:
        tote += 1
print('Há {} pessoas maiores de idade'.format(tota))
print('Há {} pessoas menores de idade'.format(tote))