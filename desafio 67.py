print('=*' * 20)
print('***** TABUADA DO ZÉ ****')
print('=*' * 20)
while True:
    numero = int(input('Digite um número para a tabuada (Digite um número negativo para parar): '))
    if numero < 0:
        break
    for multiplicador in range(1, 11):
        tabuada = numero * multiplicador
        print(f'{numero} x {multiplicador} = {tabuada}')
    print('=*' * 20)
