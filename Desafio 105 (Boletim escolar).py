#Funções do Programa
def nota(*n, sit=False):
    boletin = dict()
    boletin['Total'] = len(n)
    boletin['Nota Maior'] = max(n)
    boletin['Nota Menor'] = min(n)
    boletin['Média'] = sum(n)/len(n)
    if sit:
        if boletin['Média'] >= 7:
            boletin['Situação'] = 'Boa'
        elif boletin['Média'] >= 5:
            boletin['Situação'] = 'Razoável'
        elif boletin['Média'] < 5:
            boletin['Situação'] = 'Ruim'
    return boletin


#Programa Principal
resp = nota(5, 6, 8, 7, sit=True)
print(resp)