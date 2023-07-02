times = ('Atlético - MG', 'Flamengo', 'Palmeiras', 'Fortaleza', 'Corinthians', 'Bragantino', 'Fluminense',
         'América-MG', 'Atlético-GO', 'Santos', 'Ceará', 'Internacional', 'São Paulo', 'Athletico-PR', 'Cuiabá',
         'Juventude', 'Grêmio', 'Bahia', 'Sport', 'Chapecoense')
print(f'Os 5 primeiros colocados: {times[0:5]}')
print(f'Os quatro últims colocados: {times[-4:]}')
print(f'Em ordem alfabética:')
print(sorted(times))
print(f'Chapecoense está na posição {times.index("Chapecoense") + 1}')
