sal = float(input())

if sal <= 400:
    saln = sal * 1.15
    perc = 15
elif sal <= 800:
    saln = sal * 1.12
    perc = 12
elif sal <= 1200:
    saln = sal * 1.10
    perc = 10
elif sal <= 2000:
    saln = sal * 1.07
    perc = 7
else:
    saln = sal * 1.04
    perc = 4

print(f"Novo salario: {saln:.2f}")
print(f"Reajuste ganho: {saln - sal:.2f}")
print(f"Em percentual: {perc} %")
