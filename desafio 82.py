lista = []
lista_pares = []
lista_impares = []
while True:
    numero = int(input('Digite um número: '))
    lista.append(numero)
    parar = ' '
    while parar not in 'SN':
        parar = input('Deseja continuar? (S/N): ').upper().strip()
    if 'N' in parar:
        break
for valores in lista:
    if valores % 2 == 0:
        lista_pares.append(valores)
    else:
        lista_impares.append(valores)
print(f'Lista dos números: {lista}')
print(f'Números pares: {lista_pares}')
print(f'Números ímpares: {lista_impares}')