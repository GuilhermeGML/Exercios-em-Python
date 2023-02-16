soma = 0
perg = 's'
cont = 0
maior = 0
menor = 0
while perg != 'N':
    num = int(input('Digite um número: '))
    soma += num
    cont += 1
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    perg = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
media = soma/cont
print('A média dos termos foi {}'.format(media))
print('O maior número é {} e o menor número é {}'.format(maior, menor))