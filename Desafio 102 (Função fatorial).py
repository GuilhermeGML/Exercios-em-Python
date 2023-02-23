#Funções do Programa
def fatorial(num):
    c = n
    f = 1
    while c > 0:
        f *= c
        c -= 1
    print(f'O fatorial de {n} vale {f}')
    global fat
    fat = f


def show(r):
    from time import sleep
    if r == 'S' or 's':
        for v in range(n, 0, -1):
            print(f'{v}', end='*', flush=True)
            sleep(0.2)
        print(f'= {fat}')

#Programa Principal
n = int(input('Digite um número: '))
fatorial(n)
resp = str(input(f'Deseja ver a resolução do fatorial de {n} [S/N] = '))
show(resp)