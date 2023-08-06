cont = 0
cont_sexo = 0
media_idade = 0
maior_idade = 0
mais_velho = 0
menos_20 = 0
for p in range(1, 5):
    print('='*30)
    print(' '*10 + f'{p} Pessoa ')
    print('='*30)
    nome = str(input('Qual o seu nome: ')).strip().lower()
    idade = int(input('Qual a sua idade: '))
    sexo = str(input('Qual o seu sexo: '))
    cont += idade
    media_idade = cont / 4
    if sexo == 'f' and idade < 20:
        cont_sexo += 1
    if p == 1 and sexo == 'm':
        maior_idade = idade
        mais_velho = str(nome)
    if sexo == 'm' and idade > maior_idade:
        maior_idade = idade
        mais_velho = str(nome)

print(f'A média de idade do grupo é de {media_idade} anos')
print(f"O homem mais velho tem {maior_idade} e seu nome é {mais_velho}.")
print(f'Ao todo são {cont_sexo} mulheres com menos de 20 anos')
