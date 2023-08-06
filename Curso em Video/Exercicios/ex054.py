from datetime import date

totmaior = 0
totmenor = 0
cont = 0
hoje = date.today().year
for n in range(1, 8):
    cont += 1
    ano = int(input(f'Digite o ano de nascimento da {cont} pessoa:'))
    idade = hoje - ano
    if idade >= 18:
        totmaior += 1
    elif idade <= 18:
        totmenor += 1
print(f'{totmaior} atingiram a maioridade')
print(f'{totmenor} não atingiram a maioridade.')
