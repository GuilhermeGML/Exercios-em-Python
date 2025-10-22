nome = str(input())
sal = float(input())
vend = float(input())

com = vend * 0.15
sal += com

print(f'TOTAL = R$ {sal:.2f}')