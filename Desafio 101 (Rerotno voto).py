from datetime import date
atual = date.today().year
#Funções do programa
def voto(ano):
    idade = atual - ano
    if idade >= 18:
        return f'Sua idade é {idade}, logo teu voto é OBRIGATÓRIO'
    elif 16 <= idade < 18 or idade > 65:
        return f'Sua idade é {idade}, logo teu voto é OPICIONAL'
    elif idade < 16:
        return f'Sua idade é {idade}, logo teu voto é NEGADO'

#Programa Principal
nasc = int(input('Ano de nascimento: '))
print(voto(nasc))