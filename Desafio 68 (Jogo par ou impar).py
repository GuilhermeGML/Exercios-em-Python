from random import randint

totvit = 0
comp = randint(1, 100)
print('=+' * 20)
print('Vamos jogar PAR ou IMPAR')
print('=+' * 20)
while True:
    num = int(input('Digite um número: '))
    esc = str(input('PAR ou IMPAR: ')).strip().upper()[0]
    soma = comp + num
    if esc == 'P':
        if soma % 2 == 0:
            print('VOCÊ GANHOU')
            print(f'Você jogou {num} e o computador {comp}. Total {soma}')
            totvit += 1
        else:
            print('VOCÊ PERDEU')
            print(f'Você jogou {num} e o computador {comp}. Total {soma}')
            break
    elif esc == 'I':
        if soma % 2 == 1:
            print('VOCÊ GANHOU')
            print(f'Você jogou {num} e o computador {comp}. Total {soma}')
            totvit += 1
        else:
            print('VOCÊ PERDEU')
            print(f'Você jogou {num} e o computador {comp}. Total {soma}')
            break
print(f'Você ganhou {totvit} vezes')
