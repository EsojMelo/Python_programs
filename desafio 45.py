from random import choice
from time import sleep
parar = 0
while parar != 'f':
    print('~^~=' * 20)
    print('Vamos fazer uma brincadeira ^_^')
    print('~^~=' * 20)
    sleep(1)
    print('Conhecida como...')
    sleep(1)
    print('JOKENPÓ!!!°o°')
    r = 'Pedra'
    p = 'Papel'
    t = 'Tesoura'
    lista = [r, p, t]
    pc = choice(lista)
    print('boa sorte...(º _°)')
    sleep(2)
    pessoa = str(input('Faça a sua escolha. ( ಠ ͜ʖಠ):  '))
    print('JÓ')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PÔ!')
    sleep(1)
    print('+=+' * 20)
    print(f'Você escolheu: {pessoa}')
    print(f'O computador escolheu: {pc}')
    print('+=+' * 20)
    sleep(1)
    if (pessoa.lower() == 'tesoura' and pc.lower() == 'papel') or (pessoa.lower() == 'pedra' and pc.lower() == 'tesoura') or (pessoa.lower() == 'papel' and pc.lower() == 'pedra'):
        print(f'VOCÊ GANHOUUUU!!!\n'
        f'Voce é bom mesmo viu (@_@)\n'
        f'eu escolhi {pc}')
    elif (pc.lower() == 'tesoura' and pessoa.lower() == 'papel') or (pc.lower() == 'pedra' and pessoa.lower() == 'tesoura') or  (pc.lower() == 'papel' and pessoa.lower() == 'pedra'):
        print(f'VOCÊ PERDEU!!!\n'
        f'Parece que eu sou melhor mesmo (^ _^)\n'
        f'eu escolhi {pc}')
    elif pc.lower() == pc.lower():
        print('EMPATE')
    else: print('Tu é burro bixiga?! escreve direito.')
    parar = input('Aperte f para parar ou qualquer tecla para continuar').lower()
    if parar != 'f':

