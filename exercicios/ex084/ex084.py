'''
Faça um programa que leia nome e peso de várias pessoas, guardando
tudo em uma lista. No final, mostre:
a) Quantas pessoas foram cadastradas.
b) Uma listagem com as pessoas mais pesadas
c) Uma listagem com as pessoas mais leves.
'''
pessoas = []
dados = []

while True:
    dados.clear()
    dados.append(str(input("Nome: ")))
    dados.append(float(input("Peso: ")))

    pessoas.append(dados[:])

    resposta = str(input("Quer continuar? [S/N] ")).upper().strip()[0]
    if resposta in "Nn":
        break

maior = menor = 0

for pos, pessoa in enumerate(pessoas):
    if pos == 0:
        maior = pessoa[1]
        menor = pessoa[1]
    else:
        if pessoa[1] > maior:
            maior = pessoa[1]
        if pessoa[1] < menor:
            menor = pessoa[1]


print("-="*40)
print(f"Ao todo, você cadastrou {len(pessoas)} {"pessoa" if len(pessoas) == 1 else "pessoas"}")
print(f"O maior peso foi de {maior:.1f}Kg. Peso de", end=" ")
for pessoa in pessoas:
    if pessoa[1] == maior:
        print(f"[{pessoa[0]}]", end=" ")
print(f"\nO menor peso foi de {menor:.1f}Kg. Peso de", end=" ")
for pessoa in pessoas:
    if pessoa[1] == menor:
        print(f"[{pessoa[0]}]", end=" ")
