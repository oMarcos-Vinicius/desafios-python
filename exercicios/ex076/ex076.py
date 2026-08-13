'''
Crie um programa que tenha uma tupla única com nomes de produtos
e seus respectivo preços, na sequencia.
No final, mostre uma listagem de preços organizados os dados em 
forma tabular.
'''
lista = ("Lápis", 1.75, "Borracha", 2, "Caderno", 15.9, "Estojo", 25,
         "Tansferidor", 4.2, "Compasso", 9.99, "Mochila", 120.32,
         "Canetas", 22.3, "Livros", 34.9)

print("-"*40)
print("{:^40}".format("LISTA DE PREÇOS"))
print("-"*40)

c = 0

while c < 18:
    print(f"{lista[c]:.<31}R${lista[c+1]:>7.2f}")
    c += 2

print("-"*40)