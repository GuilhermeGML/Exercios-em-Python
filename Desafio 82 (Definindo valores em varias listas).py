lista = []
listapar = []
listaimpar = []
while True:
    lista.append(int(input('Digite um núemro: ')))
    perg = str(input('Digite um núemro: [S/N] ')).strip().upper()[0]
    if perg in 'N':
        break
for i, v in enumerate(lista):
    if v % 2 == 0:
        listapar.append(v)
    else:
        listaimpar.append(v)
print(lista)
print(listapar)
print(listaimpar)
