nome = str(input('Digite seu nome completo: ')).strip()
pn = nome.title().split()
print(f'Seu primeiro nome é: {pn[0]}')
print(f'Seu Último nome é: {pn[len(pn)-1]}')
