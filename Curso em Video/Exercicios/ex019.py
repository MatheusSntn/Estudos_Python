import random
names = []
name = input('Primeiro aluno: ')
name_2 = input('segundo aluno: ')
name_3 = input('terceiro aluno: ')
name_4 = input('quarto aluno: ')
names.append(name)
names.append(name_2)
names.append(name_3)
names.append(name_4)

print(names)
print(random.choice(names))
