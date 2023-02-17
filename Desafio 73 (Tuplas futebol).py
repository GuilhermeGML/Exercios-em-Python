time = ('Athletico Paranaense', 'Atlético', 'Atlético Mineiro', 'Grêmio', 'Corinthians',
        'Avaí', 'Ceará', 'Coritiba', 'Flamengo', 'Fluminense', 'Fortaleza', 'Goiás ', 'Internacional',
        'Palmeiras', 'Santos', 'São Paulo', 'Bahia', 'Botafogo', 'Sport', 'Cruzeiro')

print(f'Os Cinco primeiros colocados foram {time[0:5]}')
print('-=' * 25)
print(f'Os ultimos 4 colocaso foram {time[-4:]:}')
print('-=' * 25)
print(f'Time em ordem alfabética: {sorted(time)}')
print('-=' * 25)
print(f'O Palmeira está na {time.index("Palmeiras")} posição')