from random import shuffle
g1 = (input('grupo 1: '))
g2 = (input('grupo 2: '))
g3 = (input('grupo 3: '))
g4 = (input('grupo 4: '))
lista = [g1, g2, g3, g4,]
shuffle(lista)
print(f'A seqeuncia feita pelo professor é : {lista}')