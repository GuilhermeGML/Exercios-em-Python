produto = float(input('Qual é o valor da compra? R$:'))
print('='*50)
print('Escolha a forma de pagamento')
print('[1] A vista dinheiro/cheque com 10% de desconto')
print('[2] A vista no cartão com 5% de desconto')
print('[3] Em 2x no cartão')
print('[4] Em 3x ou mais no cartão com 20% de desconto')
print('='*50)
op = int(input('A opção escolhida é '))
if op == 1:
    n = produto * 0.9
    print('O produto com desconto custará {}'.format(n))
elif op == 2:
    n = produto * 0.95
    print('O produto com desconto custará {}'.format(n))
elif op == 3:
    n = produto/2
    print('O produto com desconto custará {} cada parcela'.format(n))
elif op == 4:
    div = int(input('Em quantas vezes irá dividir: '))
    n = (produto * 1.2)/div
    print('O produto com desconto custará {:.2f} cada parcela'.format(n))
else:
    print('Opção Inválida')