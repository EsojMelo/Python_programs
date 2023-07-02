from math import sqrt
a = int(input('Digite o valor de "a"'))
b = int(input('Digite o valor de "b"'))
c = int(input('Digite o valor de "c"'))
triangulo = b**2 - 4 * a * c
x1 = (-b + triangulo**1/2)  / (2 * a)
x2 = (-b - triangulo**1/2 ) / (2 * a)
print(f'O valor de delta é {triangulo}')
print(f'O valor de x1 é {x1}')
print(f'O valor de x2 é {x2}')
