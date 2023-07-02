matriz = [[],[],[]]
for f in range(0, 3):
    for c in range(0, 3):
        matriz[f].append(int(input(f'digite o termo ({f}, {c}): ')))
for f in matriz:
    for c in range(0, 3):
        print(f'[{f[c]:^5}]', end=' ')
    print()
