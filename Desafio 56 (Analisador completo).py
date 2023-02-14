media = 0
idamaior = 0
nomevelho = ''
totm = 0
for c in range(1, 5):
    print('Pessoa {}'.format(c))
    nome = str(input('Nome: ')).strip()
    sexo = str(input('Sexo [M/F]: ')).upper()
    idade = int(input('Idade: '))
    if c == 1 and sexo == 'M':
        idamaior = idade
        nomevelho = nome
    if sexo == 'M' and idade > idamaior:
        idamaior = idade
        nomevelho = nome
    if sexo == 'F' and idade < 20:
        totm += 1
media += idade
print('A média das idade é {}'.format(media/4))
print('O homem mais velho tem {} anos e se chama {}'. format(idamaior, nomevelho.upper()))
print('Há um total de {} mulheres com menos de 20 anos'.format(totm))