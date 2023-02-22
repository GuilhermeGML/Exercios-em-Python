from datetime import date
atual = date.today().year
cadastro = {}
cadastro['nome'] = str(input('Nome: '))
nasc = int(input('Data de Nascimento: '))
cadastro['idade'] = atual - nasc
cadastro['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
cadastro['sexo'] = str(input('Sexo: ')).strip().upper()[0]
if cadastro['ctps'] != 0:
    cadastro['ac'] = int(input('Ano de Contratação: '))
    cadastro['sal'] = float(input('Salário: '))
    if cadastro['sexo'] == 'M':
        cadastro['aposentadoria'] = cadastro['idade'] + ((cadastro['ac'] + 20) - atual)
    elif cadastro['sexo'] == 'F':
        cadastro['aposentadoria'] = cadastro['idade'] + ((cadastro['ac'] + 15) - atual)
print('=-' * 20)
for k, v in cadastro.items():
    print(f'{k} tem o valor de {v}')
