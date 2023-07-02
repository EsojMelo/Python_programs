lista = []
for c in range(0, 5):
    adicionar = int(input('Digite um número: '))
    if c == 0 or adicionar > max(lista):
        lista.append(adicionar)
        print(f'Valor adicionado na última posição')
    else:
        pos = 0
        while pos < len(lista):
            if adicionar <= lista[pos]:
                lista.insert(pos, adicionar)
                print(f'Valor adicionado na {pos}ª posição')
                break
            pos += 1
print(lista)
