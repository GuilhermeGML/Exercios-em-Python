import moedas
valor = float(input('Digite um valor: '))
print(f'Um aumento de 10% = {moedas.moeda(moedas.aumentar(valor, 10))}')
print(f'Um desconto de 10% = {moedas.moeda(moedas.diminuir(valor, 10))}')
print(f'O dobro de R${valor} = {moedas.moeda(moedas.dobro(valor))}')
print(f'A metade do R${valor} = {moedas.moeda(moedas.metade(valor))}')