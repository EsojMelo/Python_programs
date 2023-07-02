from random import choice, randint
# or choice
# Pode-se usar randint(1, 10)
numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
# numeros = (choice(range(0, 21)), choice(range(0, 21)), choice(range(0, 21)), choice(range(0, 21)), choice(range(0,
# 21)))
print(numeros)
print(f'O maior número é o: {max(numeros)}')
print(f'O menor número é o: {min(numeros)}')
