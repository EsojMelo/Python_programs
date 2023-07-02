maiores_idade = 0
total_homens = 0
mulheres_menores = 0
parar = ''
while parar != 'N':
    idade = int(input('Digite a idade da pessoa: '))
    sexo = input('Digite o sexo da pessoa (M/F): ').upper()
    while sexo not in 'MF':
        sexo = input('Digite o sexo da pessoa (M/F): ').upper()
    if sexo == 'M':
        total_homens += 1
    if idade >= 18:
        maiores_idade += 1
    if sexo == 'F' and idade < 20:
        mulheres_menores += 1
    parar = input('Deseja continuar? (S/N): ').upper()
    while parar not in 'SN':
        parar = input('Deseja continuar? (S/N): ').upper()
print(f'Existem {maiores_idade} pessoas maiores de idade.')
if total_homens == 1:
    print(f'Existe {total_homens} homem.')
else:
    print(f'Existem {total_homens} homens.')
print(f'Existe(m) {mulheres_menores} mulher(es) menor(es) de 20 anos.')

