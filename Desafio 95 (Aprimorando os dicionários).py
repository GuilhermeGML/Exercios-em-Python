jogador = {}
partidas = []
cadastro = []
while True:
    jogador['nome'] = str(input('Nome: '))
    tot = int(input('Partidas Jogadas: '))
    jogador['jogos'] = tot
    for g in range(0, tot):
        partidas.append(int(input('Gols marcados: ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    cadastro.append(jogador.copy())
    perg = str(input('Deseja cadastrar uma nova pessoas? [S/N] ')).upper().strip()[0]
    if perg == 'N':
        break

print('=-' * 30)
for p in cadastro:
    print('=-' * 20)
    print(f'O jogador {p["nome"]} disputou {p["jogos"]} jogos')
    for k, v in enumerate(p['gols']):
        print(f'No jogo {k+1} fez {v} gols')
    print(f'Foi um total de {p["total"]} gols')

print('=-' * 30)
print('Jogador    Gols   Total')
for p in cadastro:
    print(f'{p["nome"]}    {p["gols"]}    {p["total"]}')