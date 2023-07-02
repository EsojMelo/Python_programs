frase = str(input('Digite uma frase: ')).strip()
juntar = ''.join(frase.split())
inverter = juntar[::-1]
if inverter.upper() == juntar.upper():
    print('É um palíndromo')
else: print('Não é um palíndromo')

