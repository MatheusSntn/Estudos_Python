
active = True

while active:
    print('=' * 30)
    print('   CONVERSÃO DE TEMPERATURA')
    print('=' * 30)
    print('C para F [DIGITE C]')
    print('F para C [DIGITE F]')
    choice = input(''.upper())
    if choice == 'C':
        tempc = float(input('digite a temperatura em C:'))
        convc = tempc * 1.8 + 32
        print(f'temporatura em C: {tempc}')
        print(f'temperatura em F: {convc:.1f}')
        active = False
    elif choice == 'F':
        tempf = float(input('digite a temperatura em F:'))
        convf = (tempf - 32) / 1.8
        print(f'temporatura em F: {tempf}')
        print(f'temperatura em C: {convf:.1f}')
        active = False
    else:
        letra = input(('por favor digite C ou F: '))
        if letra == 'CF':
            active = True
