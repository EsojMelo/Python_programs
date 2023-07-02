sacar = int(input('Quanto você quer sacar: R$ '))
total = sacar
cedula = 50
total_cedulas = 0
while True:
    if total >= cedula:
        total -= cedula
        total_cedulas += 1
    else:
        if total_cedulas > 1:
            print(f'Total de {total_cedulas} cédulas de R$ {cedula}.')
        total_cedulas = 0
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        if total == 0:
            break
