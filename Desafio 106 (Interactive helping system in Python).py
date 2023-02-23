def ajuda(com):
    titulo(f'Acessando o manual')
    help(com)

def titulo(msg):
    tam = len(msg) + 4
    print(f' {msg}')


#Programa Principal
comando = ''
while True:
    titulo('SISTEMA DE AJUDA PYhELP')
    comando = str(input('Função ou Biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO!')