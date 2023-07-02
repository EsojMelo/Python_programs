lista = []
while True:
    nome = str(input('Nome: ')).strip()
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    lista.append([nome, [nota1, nota2]])
    parar = input('Deseja continuar? (S/N): ')
    if parar.upper() in 'N':
        break
print(f'{"No.":<2} \ {"NOME":<18} \ NOTA')
print('=' * 30)
for b, z in enumerate(lista):
    print(f'{f"{b}.":<2}', end=' ')
    print(f' {z[0]:<18}', end=' ')
    print(f"{(sum(z[1])) / 2:.1f}")
while True:
    escolha = int(input('Quem você quer mostrar as notas? (999 para encerrar): '))
    if escolha <= len(lista) - 1:
        print(f'O aluno {lista[escolha][0]} tem as notas: {lista[escolha][1]}')
    if escolha == 999:
        break