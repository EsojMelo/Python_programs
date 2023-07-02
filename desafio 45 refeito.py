from random import randint
from time import sleep
parar = 0
while parar != 'f':
    print('Vamos fazer uma brincadeira!!')
    sleep(1)
    print('''Escolhar qual você quer:
    [0] - PEDRA
    [1] - PAPEL
    [2] - TESOURA''')
    pessoa = int(input('Digite aqui: '))
    lista = ('pedra', 'papel', 'tesoura')
    pc = randint(0,2)
    sleep(1)
    print('JÓ')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PÔ!!!')
    sleep(1)
    print('+=+' * 20)
    print(f'Você escolheu: {lista[pessoa]}')
    print(f'O computador escolheu: {lista[pc]}')
    print('+=+' * 20)
    sleep(1)
    if (pessoa == 0 and pc == 2) or (pessoa == 1 and pc == 0) or (pessoa == 2 and pc == 1):
        print('Você GANHOU!!! PARABÉNS')
    elif (pc == 0 and pessoa == 2) or (pc == 1 and pessoa == 0) or (pc == 2 and pessoa == 1):
        print('Você PERDEU!!! ;-;')
    elif lista[pessoa] == lista[pc]:
        print('EMPATE!!!')
    else: print('Não sei que opção é essa... tente de novo.')