frase = str(input('Escreva uma frase: ')).strip()
a = frase.count('a')
A = frase.count('A')
S = a + A
print(f'Tem {S} letras A')
min = str(frase.lower())
print(f"A primeira letra a aparece em: {min.find('a')+1}")
print(f"A última letra A aparece em: {min.rfind('a')+1}")

