import datetime
nascimento = int(input('Qual o seu ano de nascimento?'))
ano = datetime.datetime.now()
idade = ano.year - nascimento
print('A sua categoria é:')
if idade <= 9:
    print('MIRIM')
elif 9 < idade <= 14:
    print('INFANTIL')
elif 14 < idade <= 19:
    print('JUNIOR')
elif 19 < idade <= 20:
    print('SÊNIOR')
elif idade <= 20:
    print('MASTER')