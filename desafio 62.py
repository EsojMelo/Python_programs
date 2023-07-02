print('Telando uma PA')
print(8 * '>-<')
primeiro_termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite o segundo termo: '))
contador = 0
adicionar = 1
termo = primeiro_termo
while contador != 10:
    termo += razao
    contador += 1
    print(f'{termo}', end=' -> ')
while adicionar != 0:
    print('PAUSE')
    adicionar = int(input('Quantos termos você quer adicionar? '))
    soma = contador + adicionar
    while contador != soma:
        termo += razao
        contador += 1
        print(f'{termo}', end=' -> ')
print('Conta feita com sucesso.')
print(f'Quantos temos você usou: {contador}')