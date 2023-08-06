n1 = float(input('Digite a nota 1: '))
n2 = float(input('Digite a nota 2: '))
media = (n1 + n2) / 2

if media < 5:
    print(f'Sua média foi {media}. Voce está reprovado.')
elif media < 6.9:
    print(f'Sua média foi {media}. Voce está de recuperacao.')
elif media >= 7:
    print(f'Sua média foi {media}. Voce está aprovado.')
