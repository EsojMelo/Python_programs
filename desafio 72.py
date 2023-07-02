numero_extensos = ('Zero', 'Um', 'Dois', 'Treis', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito',
                   'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Desesseis',
                   'Desessete', 'Desoito', 'Desenove', 'Vinte')
while True:
    escolha = int(input('Escolha um número entre 0 e 20: '))
    while escolha not in range(0, 21):
        escolha = int(input('Tente novamente. Escolha um número entre 0 e 20: '))
    print(numero_extensos[escolha])
    parar = ' '
    while parar not in 'SN':
        parar = input('Deseja continuar? [S/N]: ').upper().strip()
    if parar == 'N':
        break
