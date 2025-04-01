cod, qnt = input(). split(" ")
cod = int(cod)
qnt = int(qnt)

if cod == 1:
    tot = 4 * qnt
elif cod == 2:
    tot = 4.5 * qnt
elif cod == 3:
    tot = 5 * qnt
elif cod == 4:
    tot = 2 * qnt
elif cod == 5:
    tot = 1.5 * qnt

print(f"Total: R$ {tot:.2f}")
