while True:
    n = int(input('Qual tabuada deseja ver: '))
    if n < 0:
        break
    print('=' * 20)
    for c in range(1, 11):
        print(f'{c} x {n} = {c*n}')
    print('=' * 20)
print('FIM')