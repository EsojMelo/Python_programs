numero = int(input('Escolha um número para saber seu fatorial:'))
fatorial = numero
print(f'Calculando {numero}!', end=': ')
while numero != 1:
    print(f'{numero}', end=' x ')
    numero = numero - 1
    fatorial = fatorial * numero
print(f'{numero} = {fatorial}')