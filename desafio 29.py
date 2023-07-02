v = float(input('O carro estava a quantos km/h? '))
if v > 80:
    p = (v - 80) * 7
    print('Você foi multado por ultrapassar o limite de velocidade de 80km/h ')
    print(f'Você pagará uma multa de {p} R$')
else: print("Você estava dentro do limite de velocidade.")