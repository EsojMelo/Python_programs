soma = 0
count = 0
n = int(input('Digite um valor (999 para parar): '))
while n != 999:
    soma = soma + n
    count += 1
    n = int(input('Digite um valor (999 para parar): '))
print(f'Você digitou {count} número(s) e a soma entre ele(s) é {soma}.')
