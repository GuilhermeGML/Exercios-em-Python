dia_inicio = int(input().split()[1])
h_inicio, m_inicio, s_inicio = map(int, input().split(" : "))

dia_fim = int(input().split()[1])
h_fim, m_fim, s_fim = map(int, input().split(" : "))

inicio = s_inicio + m_inicio * 60 + h_inicio * 3600 + dia_inicio * 24 * 3600
fim = s_fim + m_fim * 60 + h_fim * 3600 + dia_fim * 24 * 3600

duracao = fim - inicio

dias = duracao // (24 * 3600)
duracao %= (24 * 3600)

horas = duracao // 3600
duracao %= 3600

minutos = duracao // 60
segundos = duracao % 60

print(f"{dias} dia(s)")
print(f"{horas} hora(s)")
print(f"{minutos} minuto(s)")
print(f"{segundos} segundo(s)")
