soma = 0
cont = 0
while True:
    valores = int(input('Digite um valor (999 para parar): '))
    if valores == 999:
        break
    soma += valores
    cont += 1
print(f'Você digitou {cont} números e a soma entre eles é {soma}')