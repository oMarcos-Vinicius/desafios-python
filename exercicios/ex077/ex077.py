'''
Crie um programa que tenho uma tupla com várias palavras (não usar acentos). 
Depois disso, você deve mostrar, para cada palavras, quais são as suas vogais.
'''

palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso',
            'gratis', 'estudar', 'praticar', 'trabalhar', 'mercado',
            'programador', 'futuro')

c = 0

while c < len(palavras):
    print(f"\nNa palavra {palavras[c].upper()} temos", end=" ")
    for letras in palavras[c]:
        if letras in "aeiou":
            print(letras,end=" ")
    c += 1