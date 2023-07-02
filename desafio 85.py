lista = [[], []]
for c in range(0, 7):
    numero = int(input(f'Digite o {c + 1}º número: '))
    if numero % 2 == 0:
        lista[0].append(numero)
    else:
        lista[1].append(numero)
print(f'Os números pares são: {sorted(lista[0])}')
print(f'Os números impares são: {sorted(lista[1])}')
