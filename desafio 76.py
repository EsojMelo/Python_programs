print('=' * 30)
print(f"{'LISTA DE COMPRAS':^30}")
print('=' * 30)
lista = ('Mandioca', 3.50, 'Peixe', 10.60, 'Pão', 4.30, 'Maçã', 2.00, 'Nootbook', 1500, 'Abacaxi', 10)
for c in range(0, len(lista)):
    if c % 2 == 0:
        print(f'{lista[c]:.<20}R$', end='')
    else:
        print(f'{lista[c]:>8.2f}')
print('=' * 30)
