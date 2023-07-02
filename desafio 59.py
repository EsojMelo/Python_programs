from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
menu = 0
while menu != '5':
    print(10 * '=+')
    print('''[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa''')
    menu = str(input('>>>> Escolha uma dessas opções: '))
    if menu == '1':
        print(f'A soma de {n1} + {n2} é {n1 + n2}')
    elif menu == '2':
        print(f'A multiplicação entre {n1} * {n2} = {n1 * n2}')
    elif menu == '3':
        if n1 > n2:
            print(f'O valor {n1} é maior que {n2}.')
        elif n2 > n1:
            print(f'O valor {n2} é maior que {n1}.')
        else:
            print('Os dois valores são iguais ')
    elif menu == '4':
        print('<<< Digite os novos valores >>>')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif menu == '5':
        print('Finalizando...')
        sleep(2)
        print(10 * '~=')
    else:
        print('Valor inválido, tente novamente.')
print('programa encerrado')


