'''
Aprimore o desafio anterior, mostrando no final:

a) A soma de todos os valores pares digitados.
b) A soma dos valores da terceira coluna
c) O maior valor da segunda linha.
'''

matriz = [[],[],[]]

for chave in range(0,3):
    for valor in range(0,3):
        matriz[chave].append(int(input(f"Digite um valor para [{chave}, {valor}]: ")))

print("-="*20)

a_soma_pares = 0
b_soma_coluna3 = 0

for chave in range(0,3):
    for valor in range(0,3):
        print(f"[ {matriz[chave][valor]} ]", end=" ")

        #a) A soma de todos os valores pares digitados.
        if matriz[chave][valor] % 2 == 0:
            a_soma_pares += matriz[chave][valor]

        #b) A soma dos valores da terceira coluna
        if valor == 2:
            b_soma_coluna3 += matriz[chave][2]

        #c) O maior valor da segunda linha.
        if chave == 1:
            if valor == 0:
                maior = matriz[chave][valor]
            else:
                if matriz[chave][valor] > maior:
                    maior = matriz[chave][valor]
    print()

print("-="*20)
print(f"A soma dos valores pares é {a_soma_pares}")
print(f"A soma dos valores da terceira coluna é {b_soma_coluna3}")
print(f"O maior valor da segunda linha é {maior}")