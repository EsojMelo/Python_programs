s = 0
c = 0
d = 0
for n in range(0, 6):
    d += 1
    p = int(input('Digite um número: '))
    if p % 2 == 0:
        s += p
        c = c + 1
print(f'Você informou {d} números')
if c == 1:
    print(f'Existe 1 número par e é igual a {s}')
elif c == 0:
    print('Não existe número(s) pares')
else:
    print(f'Existem {c} números pares e a soma deles é {s}')

