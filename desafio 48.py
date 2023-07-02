s = 0
cont = 1
for num in range(1, 501, 2):
    if num % 3 == 0:
        s += num
        cont = cont + 1
print(f'O somatorio de todos os {cont} valores solicitados é: {s}')