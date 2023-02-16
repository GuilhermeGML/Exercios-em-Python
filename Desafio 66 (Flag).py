tot = 0
soma = 0
while True:
    n = int(input('Digite um número [999 para o programa]: '))
    if n == 999:
        break
    soma += n
    tot += 1
print(f'Você digitou {tot} números e a soma ente eles foi de {soma}')