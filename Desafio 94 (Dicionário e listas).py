dados = []
cadastro = {}
idade = []
while True:
    cadastro['nome'] = str(input('Nome: '))
    cadastro['sexo'] = str(input('Sexo: ')).upper().strip()[0]
    idade.append(int(input('Idade: ')))
    cadastro['idade'] = idade
    dados.append(cadastro.copy())
    perg = str(input('Deseja cadastrar uma nova pessoas? [S/N] ')).upper().strip()[0]
    if perg == 'N':
        break
somai = sum(idade)/len(dados)
print('-=' * 20)
print(f'Foram cadastradas {len(dados)} pessoas')
print(f'A média entre as idade é {somai :.2f}')
print(f'As mulheres cadastradas foram ', end='')
for p in dados:
    if p['sexo'] == 'F':
        print(f'{p["nome"]} ', end='')
print()
print('Lista das pessoa acima da média')
for p in dados:
    if p['idade'] >= somai:
        print('   ')
        for k, v in p.itens():
            print(f'{k} = {v}; ', end='')
        print()
print('<< ENCERRANDO >>')