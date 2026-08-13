'''
Crie um programa que leia o nome e o preço de vários produtos. O
programa deverá peruntar se o usuário vai continuar. No final,
mostre:
a - Qual é o total gasto na compra
b - Quantos produtos custam mais de R$ 1000
c - Qual é o nome do produto mais barato.
'''

print("-"*30)
print("     LOJA SUPER BARATÃO    ")
print("-"*30)

a_total = 0
b_mais1000 = 0
c_barato = " "
c_preco = 0

while True:
    sair = " "
    produto = str(input("Nome do produto: ")).strip()
    preco = float(input("Preço: R$"))

    a_total += preco

    if preco >= 1000:
        b_mais1000 += 1

    if c_barato == " ":
        c_preco = preco
        c_barato = produto
    else:
        if preco < c_preco:
            c_preco = preco
            c_barato = produto

    while sair not in "SN":
        sair = str(input("Quer continuar? [S/N] ")).strip().upper()[0]

    if sair in "N":
        break

print("---------- FIM DO PROGRAMA ----------")
print(f"O total da compra foi de R${a_total:.2f}")
print(f"Temos {b_mais1000} produtos custando mais de R$1000.00")
print(f"O produto mais barato foi {c_barato} que custou R${c_preco:.2f}")