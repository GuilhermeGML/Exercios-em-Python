from UtilidadesCev import Moeda
valor = float(input('Digite um valor: '))
print(f'Um aumento de 10% = {Moeda.aumentar(valor, 10, True)}')
print(f'Um desconto de 10% = {Moeda.diminuir(valor, 10, False)}')
print(f'O dobro de R${valor} = {Moeda.dobro(valor, True)}')
print(f'A metade do R${valor} = {Moeda.metade(valor, False)}')
Moeda.resumo(valor, 30, 20)