from datetime import date
atual = date.today().year
idade = int(input('Digite seu ano de nascimento: '))
ano = atual - idade
if ano < 18:
    print('Você ainda não pode se alista')
elif ano == 18:
    print('Você pode se alistar')
else:
    print('Já passou o tempo do seu alistamento')