import numpy as np
import random

matriz = np.zeros((12, 12))
num = int(input())
op = input().upper()
soma = 0
media = 0

for l in range(12):
    for c in range(12):
        numero_aleatorio = float(input())
        matriz[l][c] = numero_aleatorio
        if c == num:
            soma = soma + matriz[l][c]

if op == "S":
    print(f"{soma}")
elif op == "M":
    print(f"{soma/12:.2f}")

