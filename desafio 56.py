media = 0
anos = 0
maisvelho = ''
mulheresojovens = 0
anos_do_mais_velho = 0
for dados in range(1, 5):
    print(f'--- {dados}° PESSOA ---')
    nome = input(f'Nome da pessoa: ')
    idade = int(input(f'Sua idade: '))
    print('''Qual o sexo? 
Digite:
1 - FEMININO
2 - MASCULINO''')
    sexo = int(input(''))
    if sexo == 1:
        sexo = 'FEMININO'
        if idade < 20:
            mulheresojovens = mulheresojovens + 1
        else:
            mulheresojovens = 0
    else:
        sexo = 'MASCULINO'
        if dados == 1:
            anos_do_mais_velho = idade
            maisvelho = nome
        if idade > anos_do_mais_velho:
            maisvelho = nome
            anos_do_mais_velho = idade
    anos = idade + anos
    print(sexo)
print(f'A média das idades é: {anos / 4}')
print(f'{maisvelho} é o mais velho e tem {anos_do_mais_velho} anos')
print(f'existe {mulheresojovens} mulheres com menos de 20 anos')
