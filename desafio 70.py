total = 0
mais_de_mil = 0
produto_barato = ''
preco_barato = 0
count = 0
while True:
    nome = input('Nome: ')
    preco = float(input('Preço: R$ '))
    if count < 1 or preco < preco_barato:
        preco_barato = preco
        produto_barato = nome
        count += 1
    total += preco
    if preco > 1000:
        mais_de_mil += 1
    parar = ' '
    while parar not in 'SN':
        parar = input('Deseja continuar? (S/N): ').upper()
    if parar == 'N':
        break
print(f'O total das compras é: {total:.2f}')
print(f'Produtos com mais de 1000 reais: {mais_de_mil}')
print(f'Produto com menor preço: {produto_barato}. Custando R$ {preco_barato}')
