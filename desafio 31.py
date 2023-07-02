D = int(input('Quantos kilômetros possuem sua viagem? '))
if D <= 200:
    vc = D * 0.5
    print(f'Você pagará {vc:.2f} R$ por essa viagem.')
else:
    vl = D * 0.45
    print(f'Você pagará {vl:.2f} R$ por essa viagem.')
