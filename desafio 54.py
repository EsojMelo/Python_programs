from datetime import date
atual = date.today().year
totmenor = 0
totmaior = 0
for pess in range(1, 8):
    nasc = int(input(f'Escreva a idade da {pess}° pessoa: '))
    idade = atual - nasc
    if idade >= 18:
        totmaior = totmaior + 1
    else:
        totmenor = totmenor + 1
print(f'Pessoas em maioridade: {totmaior}')
print(f'Pessoas em menoridade: {totmenor}')
