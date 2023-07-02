pessoa = []
dados = []
pesado = leve = 0
while True:
    dados.append(input('Nome: '))
    dados.append(float(input('Peso: ')))
    if len(pessoa) == 0:
        leve = pesado = dados[1]
    else:
        if dados[1] > pesado:
            pesado = dados[1]
        if dados[1] < leve:
            leve = dados[1]
    pessoa.append(dados[:])
    dados.clear()
    parar = input('Deseja continuar? (S/N): ').upper()
    if parar in 'Nn':
        break
print(pessoa)
print(f'Foram cadastradas {len(pessoa)} pessoas')
print(f'As pessoas com o maior peso registrado, que é {pesado}, são:', end=' ')
for p in pessoa:
    if p[1] == pesado:
        print(f'[{p[0]}]', end=' ')
print(f'As pessoas com o menor peso registrado, que é {leve}, são:', end=' ')
for p in pessoa:
    if p[1] == leve:
        print(f'[{p[0]}]', end=' ')


