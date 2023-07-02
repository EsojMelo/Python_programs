import random
from time import sleep
contador = 1
PC = int(random.randint(0, 10))
print('-=-' * 20)
print('Estou pensando em um número entre 0 e 10, será que você consegue adivinhar?')
print('-=-' * 20)
J = int(input('Que número pensei?'))
print(f'PROCESSANDO...')
sleep(2)
while J != PC:
    frases = ['Parece que você errou', 'Hum... respsota errada >_o', 'Parabéns!!! Você errou!']
    frases = random.choice(frases)
    print(frases)
    if PC > J:
        print('O valor é maior!')
    else:
        print('O valor é menor!')
    J = int(input('Digite outro valor:'))
    while J < 0 or J > 10:
        print('Digite um valor entre 0 e 10')
        J = int(input())
    contador = 1 + contador
if contador == 1:
    print('De primeira!!! Tu é fera!')
else:
    print('Parabéns!!! Agora sim você acertou!')
print(f'Você tentou {contador} vezes')



