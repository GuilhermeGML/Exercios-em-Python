def menor_carta(princesa, principe):
    todas_cartas = set(range(1, 53))
    usadas = set(princesa + principe)
    disponiveis = sorted(todas_cartas - usadas)

    def conta_vitorias(cartas1, cartas2):
        vitorias = 0
        for c1, c2 in zip(sorted(cartas1), sorted(cartas2)):
            if c1 > c2:
                vitorias += 1
        return vitorias

    for candidata in disponiveis:
        principe_completo = principe + [candidata]
        ganha_todas = True

        for p1 in princesa:
            for p2 in princesa:
                if p1 != p2:
                    for p3 in princesa:
                        if p3 != p1 and p3 != p2:
                            ordem_princesa = [p1, p2, p3]
                            if conta_vitorias(principe_completo, ordem_princesa) < 2:
                                ganha_todas = False
                                break
                    if not ganha_todas:
                        break
            if not ganha_todas:
                break

        if ganha_todas:
            return candidata

    return 1*(-1)

while True:
    dados = list(map(int, input().split()))
    if dados == [0, 0, 0, 0, 0]:
        break

    princesa = dados[:3]
    principe = dados[3:]
    print(menor_carta(princesa, principe))
