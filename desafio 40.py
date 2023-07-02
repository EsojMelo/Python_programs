nota1 = float(input('\033[1;36mDigite sua 1° nota: '))
nota2 = float(input('Digite sua 2° nota:\033[m '))
media = (nota1 + nota2) / 2
if media < 5 :
    print(f'\033[31mA sua média é {media:.2f}. Está abaixo do requerido,\n'
          f'\033[1;31mREPROVADO!\033[m')
elif media <= 6.9 and media >= 5:
    print(f'Sua média é {media:.2f}\n'
          f'RECUPERAÇÃO!')
elif media >= 7:
    print(f'\033[1;32mSua média é {media}\n'
          f'VOCÊ FOI APROVADO!\033[m')
