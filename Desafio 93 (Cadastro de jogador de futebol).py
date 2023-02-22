jogador = {}
partidas = []
jogador['nome'] = str(input('Nome: '))
tot = int(input('Partidas Jogadas: '))
for g in range(0, tot):
    partidas.append(int(input('Gols marcados: ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print('=-' * 20)
print(f'O jogador {jogador["nome"]} disputou {tot} jogos')
for k, v in enumerate(jogador['gols']):
    print(f'No jogo {k+1} fez {v} gols')
print(f'Foi um total de {jogador["total"]} gols')