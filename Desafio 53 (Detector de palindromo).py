frase = str(input('Digite uma frase: ')).strip().upper()
palvara = frase.split()
junto = ''.join(palavra)
inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
print(inverso)
if inverso == junto:
    print('É palindromo')
else:
    print('Não é palindromo')
    