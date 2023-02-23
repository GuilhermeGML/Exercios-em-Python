def aumentar(n, p, formatado=False):
    '''
    :param n: Corresponde ao valor monetário digitado
    :param p: Corresponde a porcentagem de aumento
    :param formatado: Utilizado para demonstrar o valor monetário
    :return:
    '''
    t = n + (n * (p/100))
    return t if not formatado else moeda(t)


def diminuir(n, p, formatado=False):
    '''
    :param n: Corresponde ao valor monetário digitado
    :param p: Corresponde a porcentagem de decrésimo
    :param formatado: Utilizado para demonstrar o valor monetário
    :return:
    '''
    t = n - (n * (p/100))
    return t if not formatado else moeda(t)


def dobro(n, formatado=False):
    '''
    :param n: Corresponde ao valor monetário digitado
    :param formatado: Utilizado para demonstrar o valor monetário
    :return:
    '''
    t = n * 2
    return t if not formatado else moeda(t)


def metade(n, formatado=False):
    '''
    :param n: Corresponde ao valor monetário digitado
    :param formatado: Utilizado para demonstrar o valor monetário
    :return:
    '''
    t = n/2
    return t if not formatado else moeda(t)


def moeda(n=0, moeda='R$'):
    return f'{moeda} {n:>.2f}'.replace('.', ',')


def resumo(n=0, p=10, t=5):
    print('-'*20)
    print('RESUMO DO PROJETO'.center(20))
    print('-'*20)
    print(f'Preço analisado: \t{moeda(n)}')
    print(f'Aumento de {p}% = \t{aumentar(n, p, True)}')
    print(f'Desconto de {t}% = \t{diminuir(n, t, True)}')
    print(f'Dobro do preço = \t{dobro(n, True)}')
    print(f'Metade do preço = \t{metade(n, True)}')
    print('-'*20)