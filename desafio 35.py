print('-=-' * 20)
print('Analisador de triângulos')
print('-=-' * 20)
x = float(input('1° lado do triângulo: '))
y = float(input('2° lado do triângulo: '))
z = float(input('3° lado do triângulo: '))
if (x + y) > z and (x + z) > y and (z + y) > x:
    print('É possivel forma um triângulo')
else:
    print('Não é possível formar um triângulo')