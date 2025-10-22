dias = int(input('Alugou por quantos dias:'))
km = float(input('Percorreu quantos kilometros:'))
p = (dias * 60) + (km * 0.15)
print('O total a se pagar é de {} reais'.format(p))