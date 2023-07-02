import datetime
nascimento = int(input('\033[1;34mInforme o ano de seu nascimento:\033[m '))
ano = datetime.datetime.now()
idade = ano.year - nascimento
temporestante = 18 - idade
tempopassado = idade - 18
somatempo = (18 - idade) + ano.year
subtraitempo = ano.year - (idade - 18)
if 18 > idade:
    print('\033[5;35Ainda vai se alistar para o serviço militar: ')
    print(f'Falta {temporestante} anos ({somatempo} será o ano de alistamento).\033[m')
elif (18 or 17) == idade:
    print('\033[1;32mEstá na hora do alistamento militar.\n'
          'Acesse nosso site: https://alistamento.eb.mil.br/\033[m')
elif 18 < idade:
    print(f'\033[4;31mJá passou o tempo do seu alistamento.\n'
          f'Se passaram {tempopassado} anos do seu ano ({subtraitempo}) de alistamento\033[m')
