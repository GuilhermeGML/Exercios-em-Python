print('='*20)
print('CONVERSOR DE NUMEROS')
print('='*20)
num = int(input('Digite um número: '))
print('Escolha a opção de conversão')
print('[1] Binário')
print('[2] Octal')
print('[3] Hexadecimal')
op = int(input('Qual é a opção escolhida: '))
if op == 1:
    print('O numero {} em Binário fica {}'.format(num, bin(num)[2:]))
elif op == 2:
    print('O numero {} em Octal fica {}'.format(num, oct(num)[2:]))
elif op == 3:
    print('O numero {} em Hexadecimal fica {}'.format(num, hex(num)[2:]))
else:
    print('Opção inválida')
