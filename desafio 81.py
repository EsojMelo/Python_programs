lista = []
while True:
    numero = int(input('Digite um número: '))
    lista.append(numero)
    parar = ' '
    while parar not in 'SN':
        parar = input('Deseja continuar? (S/N): ').upper().strip()
    if 'N' in parar:
        break
print(f'Foram digitados {len(lista)} números')
print(sorted(lista, reverse=True))
if 5 in lista:
    print('O número "CINCO" está na lista e está na posição: ', end='')
    for c, valores in enumerate(lista):
        if 5 == valores:
            print(c + 1, end='... ')
else:
    print('Não existe o número "cinco" na lista.')



