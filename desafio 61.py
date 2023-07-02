print('Telando uma PA')
print(8 * '>-<')
primeiro_termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite o segundo termo: '))
contador = 0
while contador != 0:
    PA = primeiro_termo + contador * razao
    contador += 1
    print(f'{PA}', end=' -> ')
print('Process finished')


