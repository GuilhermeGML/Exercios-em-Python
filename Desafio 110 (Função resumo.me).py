import moedas
valor = float(input('Digite um valor: '))
print(f'Um aumento de 10% = {moedas.aumentar(valor, 10, True)}')
print(f'Um desconto de 10% = {moedas.diminuir(valor, 10, False)}')
print(f'O dobro de R${valor} = {moedas.dobro(valor, True)}')
print(f'A metade do R${valor} = {moedas.metade(valor, False)}')
moedas.resumo(valor, 10)