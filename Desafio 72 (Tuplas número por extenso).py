num = ('Zero', 'Um', 'Dois', 'Tres', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez',
        'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezesete', 'Dezoito',
       'Dezenove', 'Vinte')
while True:
    perg = int(input('Digite um número entre 0 e 20: '))
    if perg > 20:
        print('Tente Novamente')
    else:
        break
print(f'O numero {perg} por extenso fica {num[perg]}')
