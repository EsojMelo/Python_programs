x = int(input('Escolha um número: '))
y = int(input('Escolha um segundo número: '))
z = int(input('Escolha um terceiro número: '))
maior = x
if y > x and y > z:
    maior = y
if z > x and z > y:
    maior = z
menor = x
if y < x and y < z:
    menor = y
if z < x and z < y:
    menor = z
print(f'O maior valor é : {maior}')
print(f'O menor valor é : {menor}')