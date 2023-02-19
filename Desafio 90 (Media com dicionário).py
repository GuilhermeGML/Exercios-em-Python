escola = {}
escola['Aluno'] = str(input('Nome: ')).upper()
escola['Media'] = float(input('Média: '))
if escola['Media'] >= 7:
    escola['Aprovação'] = 'Aprovado'
elif 5<= escola['Media'] < 7:
    escola['Aprovação'] = 'Recuperação'
else:
    escola['Aprovação'] = 'Reprovado'
print('=-' * 20)
for k, v in escola.items():
    print(f'{k} é igual a {v}')