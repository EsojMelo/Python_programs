maior = 0
menor = 0
posicao = 0
for pessoa in range(1, 6):
    peso = float(input(f'Digite o peso da {pessoa}° pessoa: '))
    if pessoa == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso

        if peso < menor:
            menor = peso
print(f'O mais pesado tem {maior}kg')
print(f'O mais leve tem {menor}kg')
print()


