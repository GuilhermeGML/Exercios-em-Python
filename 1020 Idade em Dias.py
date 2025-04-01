dias = int(input())
ano = 0
mes = 0
if dias >= 365:
    while dias >= 365:
        dias -= 365
        ano += 1
if dias >= 30:
    while dias >= 30:
        dias -= 30
        mes += 1
print(f"{ano} ano(s)")
print(f"{mes} mes(es)")
print(f"{dias} dia(s)")