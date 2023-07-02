n = int(input('Primeiro termo: '))
r = int(input('Digite sua razão: '))
print('Os 10 primeiros termos são:')
for PA in range(0, 10):
    an = n + PA * r
    print(f'{an}', end=' > ')
print('ACABOU')

