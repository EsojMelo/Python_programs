matriz = [[],[],[]]
pares = terceira_culuna = 0
for f in range(0, 3):
    for c in range(0, 3):
        matriz[f].append(int(input(f'digite o termo ({f}, {c}): ')))
for f in matriz:
    for c in range(0, 3):
        print(f'[{f[c]:^5}]', end=' ')
        if f[c] % 2 == 0:
            pares += f[c]
        if c == 2:
            terceira_culuna += f[c]
    print()
print(f'Soma dos valores pares é {pares}')
print(f'Soma dos valores da terceira coluna é {terceira_culuna}')
print(f'O maior valor da segunda linha é {max(matriz[1])}')
