print('-='*15)
print('   ANÁLISE DE TRIÂNGULOS')
print('-='*15)
r1 = float(input('Primeiro lado : '))
r2 = float(input('Segundo lado:'))
r3 = float(input('Terceiro lado:'))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos podem formar Triângulo')
    if r1 == r2 == r3:
        print('O triângulo formado é EQUILÁTERO')
    elif r1 != r2 != r3 != r1:
        print('O triângulo formado é ESCALENO')
    else:
        print('O triângulo formado é ISÓSCELES')
else:
    print('Os segmentos não podem formar Triângulo')