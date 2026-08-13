'''
Crie um programa que crie uma matriz de dimensão 3x3 e preencha com
valores lidos pelo teclado.

No final, mostre a matriz na tela, com a formatação correta.
'''

matriz = [[],[],[]]

for chave in range(0,3):
    for valor in range(0,3):
        matriz[chave].append(int(input(f"Digite um valor para [{chave}, {valor}]: ")))

print("-="*20)

for chave in range(0,3):
    for valor in range(0,3):
        print(f"[ {matriz[chave][valor]} ]", end=" ")
    print()