peso = float(input('Qual o seu peso? '))
altura = float(input('Qual a sua altura: '))
imc = peso / altura**2
print(f'Seu imc é {imc:.2f}, você está:')
if imc < 18.5:
    print('Abaixo do peso')
elif 18.5 <= imc < 25:
    print('Com o peso ideal')
elif 25 <= imc <= 30:
    print('em sobrepeso')
elif 30 < imc <= 40:
    print('Com obesidade')
elif imc > 40:
    print('em estado crítico de obsidade mórbida')
