qnt = int(input())
vet = [qnt]
menor = 10000
pos = 0
for i in range(qnt):
    num = int(input())
    vet.append(num)
    if num < menor:
        menor = num
        pos = i

print(f"Menor valor: {menor}")
print(f"Posicao: {pos}")
