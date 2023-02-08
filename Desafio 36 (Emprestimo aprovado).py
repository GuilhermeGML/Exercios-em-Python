din = float(input('Qual é seu salário: '))
casa = float(input('Qual o valor da casa: '))
anos = int(input('Em quantos anos deseja pagar: '))
porcentagem = (din * 30)/100
meses = anos * 12
prestação = casa/meses
if prestação <= porcentagem:
    (print('O empréstimo sera feito'))
    (print('O valor a ser pago mensalmente é de {:.2f}'.format(prestação)))
else:
    (print('Infelizmente não será possivel o empréstimo'))