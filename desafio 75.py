numeros = (int(input('Digite o 1° valor: ')), int(input('Digite o 2° valor: ')),
           int(input('Digite o 3° valor: ')), int(input('Digite o 4° valor: ')))

print(f'Você digitou: {numeros}')
print(f'O valor 9 apareceu {numeros.count(9)} vezes')
if 3 not in numeros:
    print(f'O valor 3 não foi digitado')
else:
    print(f'O valor 3 está na posição {numeros.index(3) + 1}')
print('Os números pares são: ', end='')
for c in numeros:
    if c % 2 == 0:
        print(c, end=' ')

