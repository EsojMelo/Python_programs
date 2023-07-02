from math import sin,cos,tan, radians
c = float(input('Escolha um ângulo qualquer: '))
s = sin(radians(c))
co = cos(radians(c))
tg = tan(radians(c))
print(f'seu seno é {s:.2f}')
print(f'seu cosseno é {co:.2f}')
print(f'sua tangente é {tg:.2f}')
