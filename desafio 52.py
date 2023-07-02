s = 0
n = int(input('Digite um número: '))
for d in range(1, n + 1):
    if n % d == 0:
        print(f'\033[36m', end=' ')
        s += 1
    else:
        print(f'\033[33m', end=' ')
    print(f'{d} ', end=' ')
if s == 2:
    print('\nÉ um número primo')
else:
    print('Não é um número primo')
