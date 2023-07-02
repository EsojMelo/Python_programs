nome = str(input('nome: ')).strip()
print(f'seu nome em maiúsculo : {nome.upper()}')
print(f'Seu nome em menúsculo : {nome.lower()}')
d = ''.join(nome.split())
print(f'a quantidade de letras do seu nome é {len(d)}')
dividido = nome.split()
print(f' seu primeiro nome é {dividido[0]} e a quantidades de letras é {len(dividido[0])}')

