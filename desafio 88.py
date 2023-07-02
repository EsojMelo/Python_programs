from random import randint
from time import sleep
print('=' * 30)
print(f'{"JOGO NA MEGA SENA":^30}')
print('=' * 30)
coluna = []
fileira = []
escolha = int(input('Quantos jogos vão ser sorteados? '))
print(f'{f"SORTEANDO {escolha} JOGOS":*^30}')
print('=' * 30)
for f in range(0, escolha):
    for c in range(0, 6):
        numero = randint(0, 60)
        while numero in coluna:
            numero = randint(0, 60)
        coluna.append(numero)
    fileira.append(coluna[:])
    coluna.clear()
for p, jogos in enumerate(fileira):
    print(f'Jogo {p + 1}: {sorted(jogos)}')
    sleep(1)
print(f"{' < BOA SORTE > ':=^30}")