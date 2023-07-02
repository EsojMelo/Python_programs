lista = []
while True:
    adicionar = int(input('Digite um número: '))
    if adicionar not in lista:
        lista.append(adicionar)
        print('Valor adicionado')
    else:
        print('Valor já existente. Não é possível cadastrar')
    parar = ' '
    while parar not in 'SN':
        parar = input('Deseja continuar (S/N) ? ').strip().upper()
    if 'N' in parar.upper():
        break
print(sorted(lista))



