km = float(input('Quantos kilômetros o carro percorreu?: '))
d = float(input('Quantidade de dias que o carro foi alugado: '))
rodado = 0.15 * km
alugado = 60 * d
S = rodado + alugado
print(f'O total a pagar pelo(s) {km}km pecorrido(s) durante {d} dias é {S}')