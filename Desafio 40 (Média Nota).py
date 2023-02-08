n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print('Quem tirou nota {}'.format(m))
if m >= 7:
    print('Você está APROVADO')
elif 6.9 >= m >= 5:
    print('Você está RECUPERAÇÃO')
else:
    print('Você está REPROVADO')