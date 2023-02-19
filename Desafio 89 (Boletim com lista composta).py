ficha = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('NOta 1: '))
    nota2 = float(input('NOta 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    perg = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if perg in 'N':
        break

print('-=' * 30)
print(f'{"No.":<4} {"Nome":<10} {"Média":>8}')
print('-' * 26)
for i, a in enumerate(ficha):
    print(f'{i:<4} {a[0]:<10} {a[2]:>8.1f}')
while True:
    print('-' * 26)
    opc = int(input('Mostrar nota de qual aluno? [999 para parar] '))
    if opc == 999:
        print('FINALIZANDO ...')
        break
    if opc <= len(ficha) - 1:
        print(f'No,tas de {ficha[opc][0]} sao {ficha[opc][1]}')
print('VOLTE SEMPRE')