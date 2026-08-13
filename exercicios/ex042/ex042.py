'''
Refaça o Desafio 035 dos triângulos, acrescentando o recurso de mostrar que 
tipo de triângulo será formado:

- Equilátero: Todos os lados são iguais
- Isósceles: dois lados iguais.
- Escaleno: todos os lados são diferentes.
'''

print("-=" * 30)
print("Analisador de triângulo")
print("-=" * 30)

seg1 = float(input("Primeiro segmento: "))
seg2 = float(input("Segundo segmento: "))
seg3 = float(input("Terceiro segmento: "))


if ((seg1 + seg2) > seg3) and ((seg1 + seg3) > seg2) and ((seg2 + seg3) > seg1):
    print("Os segmentos acima PODEM FORMAR um triângulo", end=' ')
    if (seg1 == seg2) and (seg2 == seg3):
        print("EQUILÁTERO!")
    elif (seg1 == seg2) or (seg2 == seg3) or (seg3 == seg1):
        print("ISÓSCELES!")
    else:
        print("ESCALENO!")
else:
    print("Os segmentos acima NÃO PODEM FORMAR um triângulo")
