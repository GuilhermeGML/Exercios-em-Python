import moedas
valor = float(input('Digite um valor: '))
print(f'Um aumento de 10% = {moedas.aumentar(valor, 10):.2f}')
print(f'Um desconto de 20% = {moedas.diminuir(valor, 20):.2f}')
print(f'O dobro de {valor} = {moedas.dobro(valor):.2f}')
print(f'A metade do {valor} = {moedas.metade(valor):.2f}')