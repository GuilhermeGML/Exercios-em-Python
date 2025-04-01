hi, mi, hf, mf = input().split()
hi = int(hi)
mi = int(mi)
hf = int(hf)
mf = int(mf)

horas = 0
minutos = 0

if hf > hi and mf >= mi:
    horas = hf - hi
    minutos = mf - mi
elif hf > hi and mf < mi:
    horas = (hf - hi) - 1
    minutos = 60 - (mi - mf)
elif hf < hi and mf >= mi:
    horas = 24 - (hi - hf) - 1
    minutos = mf - mi
elif hf < hi and mf < mi:
    horas = 24 - (hi - hf) - 1
    minutos = 60 - (mi - mf)
elif hf == hi and mf == mi:
    horas = 24
    minutos = 0

print(f"O JOGO DUROU {horas} HORA(S) E {minutos} MINUTO(S)")

