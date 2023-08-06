import random

number = (random.randint(0, 10), random.randint(0, 10), random.randint(0, 10), random.randint(0, 10), random.randint(0, 10))
print(number)
print(f'o maior valor é {max(number)}')
print(f'o menor valro é {min(number)}')