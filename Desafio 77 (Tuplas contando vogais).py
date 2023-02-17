lista = ('uva', 'laranja', 'maça', 'pera', 'melao', 'pitaya', 'melancia')
for c in lista:
    print(f'\nNa palavra {c.upper()} as vogais são ', end='')
    for letra in c:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')