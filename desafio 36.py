from time import sleep
casa = float(input('\033[33mQual o valor da casa? R$'))
salario = float(input(('Qual o salário? R$')))
anos = float(input('Quantos anos?\033[m '))
meses = anos * 12
print(f'calculando', end='')
sleep(1)
print('.', end='')
sleep(1)
print('.', end='')
sleep(1)
print('.')
print(f'Esta dividido em {casa / (casa / meses)} meses ({anos} anos) em prestações de R${casa / meses:.2f}\033[m')
m = salario * 0.30
d = casa / meses
if salario * 0.30 < casa / meses :
    print(f'\033[31mCompra negada, o valor máximo da prestação para compra é R${m}.\033[m')
else: print(f'\033[32mEmpréstimo pode ser concedido.\033[m')
