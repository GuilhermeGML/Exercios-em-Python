peso = float(input('Qual é seu peso: '))
altura = float(input('Qual é sua altura: '))
imc = peso / altura**2
if imc < 18.5:
    print('Você está ABAIXO do PESO')
elif 18.5 <= imc < 25:
    print('Você está no PESO IDEAL')
elif 25 <= imc < 30:
    print('Você está com SOBREPESO')
elif 30 <= imc < 40:
    print('Você está com OBESIDADE')
else:
    print('Você está com OBESIDADE MÓRBIDA')
