'''
Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as 
suas respectivas posições na lista.
'''
numeros = []

for c in range(0,5):
    numeros.append(int(input(f"Digite um valor para a posição {c}: ")))
    if c == 0:
        maior = menor = numeros[c]
    else:
        if numeros[c] > maior:
            maior = numeros[c]
        if numeros[c] < menor:
            menor = numeros[c]


print("Você digitou os valores", numeros)

print(f"O maior valor digitado foi {maior} nas posições", end=" ")
for pos, valor in enumerate(numeros):
    if valor == maior:
        print(f"{pos}...", end=" ")

print(f"\nO menor valor digitado foi {menor} nas posições", end=" ")
for pos, valor in enumerate(numeros):
    if valor == menor:
        print(f"{pos}...", end=" ")

    