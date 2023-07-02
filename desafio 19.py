from random import choice
p1 = str(input('Aluno 1: '))
p2 = str(input('Aluno 2: '))
p3 = str(input('Aluno 3: '))
p4 = str(input('Aluno 4: '))
lista = [p1,p2,p3,p4]
escolhido = choice(lista)
print(f'o escolhido pelo professor para apagar o quadro é : {escolhido}')