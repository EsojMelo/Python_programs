print(f'{"Lojas Zé":=^40}')
produto = float(input('Qual o preço das compras: '))
print('''formas de pagamento:
[1] - à vista dinheiro/cheque: 10% de desconto
[2] - à vista no cartão: 5% de desconto
[3] - em até 2x no cartão: preço normal
[4] - 3x ou mais no cartão: 20% de juros''')
n = int(input('Escolha entre essas 4 opções: '))
if n == 1:
    p = produto * 0.9
    print(f'O valor do produto à vista dinheiro/cheque é: R${p}')
elif n == 2:
    p = produto * 0.95
    print(f'o valor do produto à vista no cartão: R${p}')
elif n == 3:
    parcelas = produto / 2
    print(f'Está dividido em 2 parcelas de R${parcelas}')
elif n == 4:
    parcelas = int(input('Dividir em quantas vezes?'))
    divisões = (produto/parcelas) * 1.20
    total = produto * 1.20
    print(f'Você pagará {parcelas} parcelas de R${divisões:.2f} com juros')
    print(f'O valor total ficou RS{total}')
else: print('Não escolheu uma forma de pagamento, tente novamente.')