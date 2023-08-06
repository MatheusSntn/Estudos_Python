from datetime import date
'''ano = int(input('digite o ano em que voce nasceu: '))
cont = 2022 - ano

if cont < 18:
    cont_2 = 18 - cont
    print(f'Faltam {cont_2} anos para voce se alistar')
if cont > 18:
    print('Voce ja deveria ter se alistado')
elif cont == 18:
    print('está na hora de se alistar')'''

atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print(f'quem nasceu em {nasc} tem {idade} em {atual}')
if idade == 18:
    print('Voce tem que se alistar IMEDIAMENTE!')
elif idade > 18:
    cont = idade - 18
    print(f'Voce deveria ter se alistado há {cont} anos.')
    ano_alistamento = atual - cont
    print(f'voce deveria ter se alistado em {ano_alistamento}')
elif idade < 18:
    cont = 18 - idade
    print(f'Restam {cont} anos para voce se alistar.')
    ano_alistamento = atual + cont
    print(f'seu alistamento sera em {ano_alistamento}.')
