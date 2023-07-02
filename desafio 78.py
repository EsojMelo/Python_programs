numeros = []
for posicao in range(0, 5):
    numeros.append(int(input(f'Digite um número para a {posicao + 1}ª posição: ')))
maior = max(numeros)
menor = min(numeros)
print(f'O maior valor digitado é {maior} e está na posição', end=' ')
if numeros.count(maior) > 1:
    for c, valores in enumerate(numeros):
        if valores == maior:
            print(c + 1, end="... ")
else:
    print(numeros.index(maior))
print(f'\nO menor valor digitado é {menor} e está na posição', end=' ')
if numeros.count(menor) > 1:
    for c, valores in enumerate(numeros):
        if valores == menor:
            print(c + 1, end="... ")
else:
    print(numeros.index(menor))
