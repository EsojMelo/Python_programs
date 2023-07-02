x = int(input('Digite o primeiro número: '))
y = int(input('Digite o segundo número: '))
if x > y:
    print(f'O primeiro valor que é {x} é maior,')
elif y > x:
    print(f'O segundo valor que é {y} é maior')
elif y == x:
    print(f'Não existe valor maior ou menor, os dois são iguais a {x}')