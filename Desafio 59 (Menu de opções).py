num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
maior = 0
print(''' ESCOLHA UM DAS OPÇÔES
            [1] Soma
            [2] Multiplicar
            [3] Maior
            [4] Novos números
            [5] Sair do programa''')
op = int(input('Opção -> '))
while op != 5:
    if op == 1:
        print('A soma entre {} e {} resulta em {}'.format(num1, num2, num1+num2))
        print(''' ESCOLHA UM DAS OPÇÔES
                [1] Soma
                [2] Multiplicar
                [3] Maior
                [4] Novos números
                [5] Sair do programa''')
        op = int(input('Opção -> '))
    elif op == 2:
        print('A multiplicação entre {} e {} resulta em {}'.format(num1, num2, num1*num2))
        print(''' ESCOLHA UM DAS OPÇÔES
                [1] Soma
                [2] Multiplicar
                [3] Maior
                [4] Novos números
                [5] Sair do programa''')
        op = int(input('Opção -> '))
    elif op == 3:
        if num1 > num2:
            maior = num1
        else:
            maior = num2
        print('O Maior numero é {}'.format(maior))
        print(''' ESCOLHA UM DAS OPÇÔES
                [1] Soma
                [2] Multiplicar
                [3] Maior
                [4] Novos números
                [5] Sair do programa''')
        op = int(input('Opção -> '))
    elif op == 4:
        print('Os novos numeros são')
        num1 = int(input('Digite um número: '))
        num2 = int(input('Digite outro número: '))
        print(''' ESCOLHA UM DAS OPÇÔES
                [1] Soma
                [2] Multiplicar
                [3] Maior
                [4] Novos números
                [5] Sair do programa''')
        op = int(input('Opção -> '))
print('O programa terminou')
print('FIM')