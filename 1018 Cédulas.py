dinheiro = int(input())
n_100 = 0
n_50 = 0
n_20 = 0
n_10 = 0
n_5 = 0
n_2 = 0
n_1 = 0
print(f"{dinheiro}")
if dinheiro >= 100:
    while dinheiro >= 100:
        dinheiro -= 100
        n_100 += 1
if dinheiro >= 50:
    while dinheiro >= 50:
        dinheiro -= 50
        n_50 += 1
if dinheiro >= 20:
    while dinheiro >= 20:
        dinheiro -= 20
        n_20 += 1
if dinheiro >= 10:
    while dinheiro >= 10:
        dinheiro -= 10
        n_10 += 1
if dinheiro >= 5:
    while dinheiro >= 5:
        dinheiro -= 5
        n_5 += 1
if dinheiro >= 2:
    while dinheiro >= 2:
        dinheiro -= 2
        n_2 += 1
if dinheiro >= 1:
    while dinheiro >= 1:
        dinheiro -= 1
        n_1 += 1


print(f"{n_100} nota(s) de R$ 100,00")
print(f"{n_50} nota(s) de R$ 50,00")
print(f"{n_20} nota(s) de R$ 20,00")
print(f"{n_10} nota(s) de R$ 10,00")
print(f"{n_5} nota(s) de R$ 5,00")
print(f"{n_2} nota(s) de R$ 2,00")
print(f"{n_1} nota(s) de R$ 1,00")
