from time import sleep


def linha():
    print(30 * '-=')


def contador(i, f, p):
    linha()
    if p < 0:
        print(f'Contagem de {i} até {f} de {-p} em {-p}')
    elif p == 0:
        print(f'Contagem de {i} até {f} de 1 em 1')
    else:
        print(f'Contagem de {i} até {f} de {p} em {p}')
    if i < f and (p == 0 or p > 0):
        for t in range(i, f + 1, p):
            print(t, end=' ')
            sleep(0.4)
        print('FIM!')
    elif i > f and p > 0:
        for t in range(i, f - 1, -p):
            print(t, end=' ')
            sleep(0.4)
        print('FIM')
    elif i > f and p < 0:
        for t in range(i, f - 1, p):
            print(t, end=' ')
            sleep(0.4)
        print('FIM')
    elif i > f and p == 0:
        for t in range(i, f - 1, -1):
            print(t, end=' ')
            sleep(0.4)
        print('FIM')

linha()
for c in range(0, 11):
    print(c, end=' ')
    sleep(0.4)
print('FIM')
linha()
for c in range(10, -2, -2):
    print(c, end=' ')
    sleep(0.4)
print('FIM')
linha()
contador(int(input(f'{"Início:":<8} ')), int(input(f'{"Fim:":<8} ')), int(input(f'{"Passo:":<8} ')))
