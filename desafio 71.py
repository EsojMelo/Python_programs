print('=' * 30)
print('{:*^30}'.format('BANCO DO ZÉ'))
print('=' * 30)
sacar = int(input('Quanto você quer sacar: R$ '))
cedulas_cinquenta = cedulas_vinte = cedulas_dez = cedulas_um = 0
cedulas = 0
while cedulas != sacar:
    if cedulas + 50 > sacar:
        if cedulas + 20 > sacar:
            if cedulas + 10 > sacar:
                if cedulas + 1 > sacar:
                    break
                else:
                    cedulas += 1
                    cedulas_um += 1
            else:
                cedulas += 10
                cedulas_dez += 1
        else:
            cedulas += 20
            cedulas_vinte += 1
    else:
        cedulas += 50
        cedulas_cinquenta += 1
if cedulas_cinquenta > 0:
    print(f'{cedulas_cinquenta} cédulas de 50 ')
if cedulas_vinte > 0:
    print(f'{cedulas_vinte} cédulas de 20')
if cedulas_dez > 0:
    print(f'{cedulas_dez} cédulas de 10')
if cedulas_um > 0:
    print(f'{cedulas_um} cédulas de 1 ')
print(30 * '=')
print('Caixa ZÉ agradece a preferência.')
