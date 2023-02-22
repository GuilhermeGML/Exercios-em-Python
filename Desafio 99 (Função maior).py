# Funções do Programa
def maior(* num):
    cont = maior = 0
    print('-=' * 20)
    print('Analisando os valores passados ...')
    for valor in num:
        print(f'{valor} ', end='', flush=True)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informados {cont} valores ao todos.')
    print(f'O maior valor informados foi {maior}')
    print('-=' * 20)


#Programa Principal
maior(5, 2, 3, 6, 8, 9)
maior(5, 7, 6, 2, 1)
