numero = 0
total = 0
mes = 0
while True:
    numero += 1
    ganho = float(input(f"Digite O {numero}° ganho: "))
    total += ganho
    mes = int(input("qual o mês em número: "))
    if ganho == 0:
        break
print(f'Você obteve um ganho total de {total} durante {mes} meses')
media = total/mes
print(f'Sua média mensal é {media}')
