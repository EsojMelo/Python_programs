print('Telando uma PA')
print(8 * '>-<')
primeiro_termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão da PA: '))
contador = 1
total = 0
adicionar = 10
termo = primeiro_termo
while adicionar != 0:
    total += adicionar
    while total >= contador:
        print(f'{termo}', end=' -> ')
        termo += razao
        contador += 1
    print('PAUSA')
    adicionar = int(input('Quantos valores você quer adicionar? '))
print(f'Operação finalizada com {contador - 1} termos.')
