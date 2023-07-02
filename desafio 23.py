from random import randint
'''n = str(randint(0, 9999))
print(n)
print(f'Unidade: {n[3]}')
print(f'dezena: {n[2]}')
print(f'centena: {n[1]}')
print(f'milhar: {n[0]}')'''

x = int(input('Escolha um número entre 0 e 9999: '))
num = str(x)
print(f'Unidade: {num[3]}')
if num[3] == "":
    print('0')
print(f'Dezena: {num[2]}')
print(f'centena: {num[1]}')
print(f'milhar: {num[0]}')