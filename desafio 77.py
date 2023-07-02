palavras = ('Abacaxi', 'Maracuja', 'Limão', 'Acerola')
for c in palavras:
    print(f'A palavra {c.upper()} tem as vogais:', end=' ')
    for letra in c:
        if letra.lower() in 'aeiouãáêõ':
            print(letra.lower(), end=' ')
    print('')