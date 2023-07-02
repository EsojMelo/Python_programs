print('\033[1;36m-=-' * 20)
print('Analisador de triângulos')
print('-=-' * 20)
'\033[m'
x = float(input('\033[34m1° lado do triângulo: '))
y = float(input('2° lado do triângulo: '))
z = float(input('3° lado do triângulo: \033[m'))
if (x + y) > z and (x + z) > y and (z + y) > x:
    print('\033[1;32mÉ possivel formar um triângulo')
    if x == y == z:
        print('E é equilátero.')
    elif x == y or y == z or x == z:
        print('E é isóceles.')
    elif x != y != z != x:
        print('E é escaleno.\033[m' )
else:
    print('\033[1;31mNão é possível formar um triângulo\033[m')