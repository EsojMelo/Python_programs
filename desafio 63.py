print('-=' * 16)
print('*** SEQUÊNCIA DE FIBONACCI ***')
print('-=' * 16)
quantidade = int(input('Escolha quantos números você quer mostrar: '))
print('-=' * quantidade * 4)
termos = 0
primeiro_valor = 0
segundo_valor = 1
while termos < quantidade:
    print(f'{primeiro_valor}', end=' -> ')
    primeiro_valor += segundo_valor
    termos = termos + 1
    if termos == quantidade:
        break
    print(f'{segundo_valor}', end=' -> ')
    segundo_valor += primeiro_valor
    termos = termos + 1
print('Finalizado')
print('-=' * quantidade * 4)
print(termos)
