num = int(input('Escolha um número inteiro: '))
print('''Escolha uma das bases para conversão:
[1] - Converter em Binário
[2] - Converter em Octal
[3] - Converter em Hexadecimal''')
opção = int(input('Qual sua opção?'))
if opção == 1:
    binário = bin(num)
    print(f'O valor em binário é: {binário}')
elif opção == 2:
    Octal = oct(num)
    print(f'O valor em Octal é: {Octal}')
elif opção == 3:
    Hexadecimal = hex(num)
    print(f'O valor em Hexadecimal é: {Hexadecimal}')
else: print('Opção inválida, tente novamente.')