#Funções do Programa
def leiaint(msg):
    ok = True
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('ERRO! Digite um número válido')
        if ok:
            break
    return valor


#Programa Principal
n = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {n}')