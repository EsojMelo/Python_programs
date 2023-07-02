from random import choice


def sorteia(a, b):
    lista = list(range(a, b))
    numeros = []
    print("Sorteando 5 valores da lista: ", end=' ')
    for c in range(0, 5):
        escolhidos = choice(lista)
        print(f"{escolhidos}", end=" ")
        numeros.append(escolhidos)
    return numeros


def somapar(numeros):
    add = 0
    for p in range(0, 5):
        x = numeros[p]
        if x % 2 == 0:
            add = x + add
    print(f"\nSomando os valores pares de {numeros} temos: {add}")


numeros = sorteia(0, 10)
somapar(numeros)