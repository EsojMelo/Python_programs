import random
from time import sleep
PC = str(random.randint(0,5))
print('-=-' * 20)
print('Estou pensando em um número entre 0 e 5, será que vc acerta?')
print('-=-' * 20)
J = str(input('Que número pensei...?'))
print(f'PROCESSANDO...')
sleep(3)
print('PAM PAM PAM PAAAAMMMM...')
sleep(2)
if J == PC:
    print('PARABÉNS! Você ganhou!')
else: print('Você perdeu! mais um ponto pra mim ^-^')
print(f'Eu escolhi o número {PC}')
input()
