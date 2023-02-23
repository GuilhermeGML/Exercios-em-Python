#Funções do Programa
def ficha(n='<desconhecido>', g=0):
    print(f'O jogador {n} fez {g} gols')


#Programa Principal
jog = str(input('Nome: '))
gol = str(input('Gols marcados: '))
if gol.isnumeric():
    gol = int(gol)
else:
    gol = 0
if jog.strip() == '':
    ficha(g=gol)
else:
    ficha(jog, gol)