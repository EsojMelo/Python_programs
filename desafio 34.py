from time import sleep
salario = float(input('Qual o salário do funcionário?'))
if salario > 1250.00:
    aumentomenor = salario * 1.10
    print('Terá um aumento de 10%')
    sleep(1)
    print(f'Calculando...')
    sleep(2)
    print(f'O aumento desse funcionário é de {aumentomenor:.2f} R$')
else:
    salario <= 1250.00
    aumentomenor = salario * 1.15
    print('Terá um aumento de 15%')
    sleep(1)
    print('Calculando...')
    sleep(2)
    print(f'O aumento desse funcionário é de {aumentomenor:.2f} R$')

