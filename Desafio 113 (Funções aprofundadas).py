def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('ERRO no valor digitado tente novamente')
            continue
        else:
            return n

def leiafloat(msg):
    while True:
        try:
            m = int(input(msg))
        except (ValueError, TypeError):
            print('ERRO no valor digitado tente novamente')
            continue
        else:
            return m

#Programa Principal
n = leiaint('Digite um número: ')
m = leiafloat('Digite um núemro:')
print(f'O valor inteiro digitado foi {n}')
print(f'O valor real digitado foi {n}')