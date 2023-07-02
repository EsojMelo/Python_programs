from random import choice
print('*=*' * 18)
print('**** VAMOS JOGAR PAR OU IMPAR ****')
print('\033[1;31m(Até você perder! HAHAHA\033[m)')
print('*=*' * 18)
count = 0
while True:
    player = int(input('Digite um número ("F" para parar): '))
    if player == 'F' or player == 'f':
        break
    escolha = 'g'
    while escolha not in 'IP':
        escolha = input('Par ou Impar? (P/I): ').upper()
    PC = int(choice(range(0, 11)))
    soma = player + PC
    print('-' * 20)
    print(f'Você escolheu {player} e o computador {PC}, a soma é {soma}')
    print('-' * 20)
    if escolha == 'P':
        if soma % 2 == 0:
            print(f'{soma} é PAR, você Ganhou!!!')
            count += 1
        else:
            print(f'{soma} é IMPAR, você perdeu!!!')
            print('Acabou pra você!')
            break
    elif escolha == 'I':
        if soma % 2 != 0:
            print(f'{soma} é IMPAR, você Ganhou!!!')
            count += 1
        else:
            print(f'{soma} é PAR, você perdeu!!!')
            print('Acabou pra você!')
            break
    print('Vamos tentar de novo!')
print(f'Você venceu {count} vez(es).')




