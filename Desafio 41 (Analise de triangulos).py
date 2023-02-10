from datetime import date
atual = date.today().year
idade = int(input('Em que ano você nasceu: '))
ano = atual - idade
if ano <= 9:
    print('Sua categoria é MIRIM')
elif 9 < ano <= 14:
    print('Sua categoria é INFANTIL')
elif 15 < ano <= 19:
    print('Sua categoria é JÚNIOR')
elif 20 < ano <= 25:
    print('Sua categoria é SÊNIOR')
else:
    print('Sua categoria é MASTER')