n = 0
tot = 0
soma = 0
while n != 999:
    n = int(input('Digite um número [999 para o programa]: '))
    if n != 999:
        soma += n
        tot += 1
print('Você digitou {} números e a soma ente eles foi de {}'.format(tot, soma))
