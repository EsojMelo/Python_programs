sexo = str(input('Digite o sexo: ')).strip().upper()[0]
while sexo not in 'FM':
    sexo = input('Sexo invalido, digite novamente: ').strip().upper()[0]