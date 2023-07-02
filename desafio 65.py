menor_valor = maior_valor = valores = 0
continuar = ''
soma = 0
count = 0
while continuar != 'n':
    valores = int(input('Digite um valor: '))
    if valores > maior_valor:
        maior_valor = valores
    elif valores < menor_valor:
        menor_valor = valores
    else:
        menor_valor = valores
        maior_valor = valores
    soma += valores
    count += 1
    continuar = str(input('Você quer continuar? ("S" para "SIM"/ "N" para "NÃO"):  ')).lower().strip()
print(f'Você digitou {count} números e a média é {soma / count:.2f}.')
if maior_valor != menor_valor:
    print(f'O maior valor é {maior_valor} e o menor {menor_valor}.')
else: 
    print(f'O menor e o maior valor são iguais a {maior_valor}')
