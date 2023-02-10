from random import randint
lista = ('Pedra', 'Tesoura', 'Papel')
computador = randint(0, 2)
print('''Escolha um número
[1] Pedra
[2] Tesoura
[3] Papel''')
jogador = int(input('Qual é a sua jogada: '))
if computador == 0:
    if jogador == 1:
        print('Você jogou PEDRA e o computador jogou PEDRA logo deu EMPATE')
    elif jogador == 2:
        print('Você jogou TESOURA e o computador jogou PEDRA logo você perdeu PERDEU')
    elif jogador == 3:
        print('Você jogou PAPEL e o computador jogou PEDRA logo você GANHOU')
if computador == 1:
    if jogador == 1:
        print('Você jogou PEDRA e o computador jogou TESOURA logo você GANHOU')
    elif jogador == 2:
        print('Você jogou TESEOURA e o computador jogou TESOURA logo deu EMPATE')
    elif jogador == 3:
        print('Você jogou PAPEL e o computador jogou TESOURA logo você PERDEU')
if computador == 2:
    if jogador == 1:
        print('Você jogou PEDRA e o computador jogou PAPEL logo você PERDEU')
    elif jogador == 2:
        print('Você jogou TESOURA e o computador jogou PAPEL logo você GANHOU')
    elif jogador == 3:
        print('Você jogou PAPEL e o computador jogou PAPEL logo deu EMPATE')
if jogador >= 4:  
    print('JOGADA INVÁLIDA TENTE NOVAMENTE')